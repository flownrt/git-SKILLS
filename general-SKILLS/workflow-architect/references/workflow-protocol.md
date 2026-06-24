# Closed-Loop Workflow Protocol (baseline)

A baseline run-time protocol: how an orchestrator should operate a multi-step task, plus the minimum review and handoff discipline any agent run should keep. It is the operating rhythm and the review/handoff layer – not a finished design. It deliberately does not encode the org chart, the worker dependency graph, or the communication topology; the Workflow Architect prescribes it as a starting point and designs the task-specific roles, wiring, and loop on top of it. Prescribe it whole, trim it for light work, or extend it, but adapt it per task and keep the blind-spot check, the independent review, and the written handoff. It assumes no particular tools, domain, or provider.

**1. Plan** – Numbered steps. Per step: action, subagent (if any), expected output. Use subagents in two cases: (a) **parallel** when steps are genuinely independent, (b) **sequential** when a step is context-heavy (large file scan, deep research, long generation) – the orchestrator only needs the subagent's summary, not its full trace. Inline only for short, light work. No speculative parallelism.

**2. Blind-spot check** – Before clarifications, answer once, honestly, in 1–3 lines: *what is the most important thing I am missing here?* Look for unstated assumptions, missing inputs, ignored constraints, edge cases, or unrepresented stakeholders. If something surfaces, fold it into the plan or into the clarifications. A reflexive "nothing" is itself a finding worth pausing on.

**3. Clarifications** – Batch all uncertainties at the end of the plan: question + proposed answer + safe default. Zero uncertainties → continue. Otherwise stop and wait.

**4. Execute** – Follow the plan. Note any deviation in one line. Stay in scope. One short progress note per step. Each subagent gets a self-contained brief (goal, inputs, expected output, success criteria) and returns a compact summary, not raw working material.

**5. Independent review** – Spawn a fresh subagent in isolation. It sees only the original request, the final outputs, and the Phase 1 plan – not the execution trace. It audits coverage, correctness, justified deviations, and scope creep. Verdict: PASS or FAIL with findings. On FAIL, dispatch targeted rework subagents and re-run the review. Max 3 cycles, then hand back.

**Final report** – Done · Skipped/deferred · Files touched · Open items · Review verdict + cycle count.
