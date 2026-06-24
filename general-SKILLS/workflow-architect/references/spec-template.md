# Workflow Spec / Brief – Template

A blank scaffold for one workflow spec, ordered so the filled copy reads top-down as an executable brief: a run header the build session acts on first, then the design a human reviews. Fill each part and delete any the right-size gate ruled out – a trivial task needs none of this; a solo redraft loop needs only the run header, Definition of done, Loop design, and Verification. Keep it proportionate: this is a contract a human signs off on *and* a fresh build session runs from, so it must stand alone – assume the builder has none of the context it was written in. Save the filled copy as `spec-brief.md` in your workflow library.

---

## Run header – the builder reads this first

- **Workflow name:** [short, reusable name]
- **Mode:** new design | improving an existing workflow
- **Goal (one line):** [what "done" looks like]
- **Build kickoff:** [the one instruction that starts the build, e.g. "Execute this brief following the baseline protocol below; pause at each human gate; halt and report if any guardrail trips."]
- **Baseline protocol to follow:** [references/workflow-protocol.md, or the named adaptation]
- **Guardrails (hard stops):** max iterations: [n] · no-progress detection: [rule] · hard ceiling: [tokens or $]
- **Budget (target, with derivation):** [cost and latency the design should fit, and how the figure was reached – e.g. ≈ work-units × per-unit cost; fan-out trades tokens for wall-clock]
- **Human gates:** [the points where a human must approve before the run continues]
- **On ambiguity:** [what the builder does when something is unclear – stop and ask, or proceed on which stated default]
- **Assets to reuse:** [existing skills, protocols, tools, data sources to call instead of reinventing]
- **Must-verify before build:** [capability assumptions the design depends on – e.g. "the warehouse supports idempotent MERGE", "an approval channel exists" – that the builder confirms true before building; distinct from the softer defaults above]
- **Diagnosis (improving mode only):** [what the current design is and where it leaks – cite items from references/failure-modes.md]

## The design – for human review before sign-off

**Definition of done** – [executable validation contract: tests to pass, outputs to parse, criteria to confirm]

**Org chart**

- Orchestrator: [owns the plan and the definition of done; never implements]
- Workers: [one scope each, clean context, in dependency order]
- Validators: [fresh eyes that never wrote the work]
- Model/tool tier per role: [optional – e.g. cheap workers, strong orchestrator/validator]
- Wiring, per transition: [pattern – delegation / creator-verifier / broadcast / negotiation]
- Shared-state surface: [what is shared, and how collisions are avoided]

**Workspace layout** – derive a structure from *this* workflow's actual artifact classes (only the ones it really produces), ordered by flow with numeric-prefix buckets so the sequence reads top-down. The convention is the numbering (`10-`, `20-`, …), not a fixed set: a stateless research run might be just `10-sources/ · 20-draft/ · 30-final/`, while a stateful pipeline might add staging, checkpoints, logs, and a registered-skills bucket. Note where a resuming step reads state back. Trim entirely for trivial tasks.

**Loop design** – [closed | open] · path: [the bespoke steps for this workflow] · eval gate per step: [...] · stop condition: [...]
(The generic run-time discipline – blind-spot, clarifications, independent review, written handoff – is the baseline protocol named in the header; record here only what is bespoke to this workflow.)

**Verification** – self-check (executable): [run / parse / confirm against ground truth] · adversarial review (fresh context): [who reviews, on what]

**Handoff format** – [what every transition records: done / not done / commands run + exit codes / issues found / procedures followed; or "the baseline protocol's contract"]

**Skill extraction** – [steps to encode as named, tested skills and register in the library]

**Diff (improving mode only)** – [the specific changes from the current setup to this spec]
