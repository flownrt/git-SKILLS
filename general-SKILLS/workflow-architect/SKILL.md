---
name: workflow-architect
description: Design closed-loop agent workflows – the definition of done, the wired org chart, the loop, the guardrails, and the handoff – as a reviewable spec a human approves before any agent runs, sized to the smallest architecture that fits. Works on a new goal or audits and improves an existing workflow, and flags steps to encode as reusable skills. Use when a task is too big for one prompt (multi-step builds, research-then-write, work meant to run unattended), when you need to design an agent team, orchestrator, subagents, the loop, or the handoff and guardrails, or when you want to audit or improve an existing workflow, pipeline, or repo's agent setup. Do NOT use for trivial single-pass tasks (just run them), for merely defining what "done" means with no agents to coordinate (that is a scoping task, not agent machinery), when the work should be executed rather than designed, or when a one-off prompt rather than a reusable spec is wanted.
---

# Workflow Architect

Turn a goal into a runnable, closed-loop agent-team design – or take an existing workflow and make it one. The deliverable is a *spec a human reviews before any agent runs*: the definition of done, the org chart and its wiring, the loop, the guardrails, and the handoff format, plus a note of which steps should become reusable skills. It is not a prompt and not a running system. Each spec is a named, reusable asset; the job is to grow a workflow library, not to author one-off prompts. Prompts expire; skills and specs compound.

This skill runs in two directions, both using the same method and the same bar for "good":

- **Designing** – given a goal, produce the smallest agent-team architecture that meets the definition of done.
- **Improving** – given an existing workflow, repo, or running setup, reconstruct its current design, run it against the failure-mode checklist ([references/failure-modes.md](./references/failure-modes.md)) to find where it leaks, and emit the corrected spec plus a short diff of what to change.

It is design-time only – it produces the design, it does not start the build. It does not launch the agent team it designs or kick off the production run; that happens later, in a separate, human-gated build session. It may, though, spawn subagents to do its *own* work – fanning out to audit a large repo or research an unfamiliar domain is context-heavy, so delegate it and keep the summary. Guardrails, stop conditions, and human gates are *prescribed in the spec*, not enforced here – the spec is the contract the eventual run is held to.

## Right-size first (the gate, always)

Before designing anything, size the task and scale the output to it. Never overengineer – proportionality is a hard rule, not a preference.

- **Trivial / single-pass** → emit "no workflow needed, run it directly." Stop.
- **One agent, bounded redraft loop** → emit a minimal loop spec: goal, eval criteria, stop condition. No org chart, no validators as separate roles.
- **Multi-agent** → the full spec below.

The architecture must be the smallest one that meets the definition of done; a solo redraft loop does not get an org chart. When improving an existing workflow this gate cuts both ways – shrink an over-built setup as readily as you harden an under-built one.

## How to run it

1. **Blind-spot check (your own), then clarify.** Before designing, audit yourself once, honestly: what is missing, what is assumed, what is unstated? Look for missing inputs, ignored constraints, edge cases, unrepresented stakeholders. A reflexive "nothing" is a sign of shallow self-audit, not an answer. Batch every genuine open question with a proposed default into a single decision point, then continue – or stop and wait if something blocks.

2. **Inventory what already exists.** List the data sources, tools, and existing skills or protocols the workflow can call. Reuse before inventing; never re-emit an asset that already exists. When improving a workflow this is also the audit input: read the current setup before judging it – and if the repo or input is large, fan the read-and-reconstruct out to subagents and work from their summaries. That is the architect doing its own context-heavy work, not launching the designed run. Separate assets you have confirmed exist from capability assumptions the design will *depend on* but you have not verified (a store supports idempotent writes, an approval channel exists) – flag the latter as must-verify-before-build, never state them as facts.

3. **Write the definition of done first.** State the validation contract in executable terms – tests to pass, outputs to parse, criteria to confirm – before any work is scoped. If you cannot imagine checking it, rewrite it until you can.

4. **Decompose into scopes with dependencies.** Break the goal into worker-sized scopes, each on clean context. A flat list is not a plan: encode explicit blocking relationships and sequencing – what must finish before what, what can run in parallel. No speculative parallelism.

5. **Draw the org chart and its edges.** Nodes without wiring is the most common silent failure. Name every role, the model or tool tier it runs on where that matters (cheap workers, a strong orchestrator or validator), and every transition between roles – tag each with its pattern: delegation (parent→sub), creator-verifier (worker→validator), broadcast (shared state→all), or negotiation (workers sharing a file, API, or codebase region). Make the shared-state surface explicit – what is shared, how parallel workers avoid colliding on it, and where state, artifacts, and logs physically live so a resuming step can read them back.

6. **Choose the loop.** Closed by default – a defined path with an eval gate at each step and an explicit stop condition. Open only when exploration is the point and the budget is unlimited.

7. **Set verification – two distinct mechanisms.** (a) An executable self-check inside the loop body: run, parse, confirm against ground truth. (b) An adversarial review by a fresh context that never wrote the work. A reader that only opines is not a gate; both are required, distinctly.

8. **Set guardrails and human gates.** Prescribe three hard stops before launch: a max iteration count, no-progress detection, and a hard token or dollar ceiling. Distinguish that ceiling (when to abort) from the cost and latency *budget* (whether the design is affordable at all – fan-out buys wall-clock with tokens), and state both – give the budget a one-line derivation (e.g. work-units × per-unit cost) so a reviewer can sanity-check it rather than trust a plucked number. Place the human-review checkpoints the constraints require.

9. **Flag skill-extraction candidates.** Mark any step that will recur, or that took real iteration to get right, to be encoded as a named, tested skill and registered in the library. For the generic run-time discipline – the orchestrator's operating rhythm, the independent review, and the written handoff – prescribe or adapt the baseline protocol in [references/workflow-protocol.md](./references/workflow-protocol.md); design the task-specific org chart and loop on top of it rather than letting the baseline stand in for them.

## What makes the spec good

- **Right-sized.** The smallest architecture that meets the definition of done wins. An org chart for a solo loop is a defect, not thoroughness.
- **The unit of work is the loop, not the prompt.** Design the path and its stop condition, not each individual step.
- **An org chart is nodes and edges.** Unwired roles collide silently and missing arrows are invisible in review. Name every transition.
- **Verification is structural, not hopeful.** Two things: an executable self-check and a fresh-eyes review. No gate means unreviewed output delivered in a confident tone.
- **State is written, not remembered.** Every handoff records what is done, what is not, the commands run and their exit codes, and the issues found.
- **The asset is the library, not the prompts.** Reuse existing skills and protocols before authoring new ones, and register what you build.

## Output

Fill the blank scaffold in [references/spec-template.md](./references/spec-template.md) so every spec in the library has the same shape and reads top-down as an executable brief – a run header the builder acts on first, then the design a human reviews. Trim any part the right-size gate ruled out. The template's parts map one-to-one onto the steps above, so fill them there rather than restating them here. The one part not already covered by a step is the **workspace layout** – a structure *derived from this workflow's own artifact classes*, ordered with numeric-prefix buckets (`10-`, `20-`, …) so the sequence reads top-down, and trimmed away for stateless tasks. The numbering is the convention; the buckets themselves are designed per workflow, never copied from a default.

When improving an existing workflow, precede the spec with a one-paragraph diagnosis (what the current design is and where it leaks) and follow it with a short diff – the specific changes to make – so the result is actionable, not just aspirational.

Write the result as a self-contained handoff – a `spec-brief.md` a fresh build session can run cold, with no memory of this one. Up front, in a run header the builder reads first, state which baseline protocol to follow, the guardrail ceilings and human gates, the assets to reuse, the capability assumptions the builder must verify first, and what to do on ambiguity (stop and ask, or proceed on a stated default); the design parts follow, for human review. The build itself then happens in that separate session, carried out by agents against this brief – which is exactly why the design is written down and reviewed first rather than executed here.

Keep the whole thing proportionate to the task and easy to review: it is the contract the eventual run is held to, and a human signs off on it before any agent starts.
