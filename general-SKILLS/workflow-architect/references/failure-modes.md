# Workflow Failure Modes – Audit Checklist

Run an existing workflow, pipeline, or agent setup against this list before redesigning it. Each entry is a way real workflows leak, paired with the design rule that fixes it – the rule the Workflow Architect would have applied. This is the diagnosis input for the skill's "improving" mode: not every item applies to every workflow, so cite only the ones that actually bite.

- **Unwired roles.** Roles are named but the transitions between them are not; nodes without edges collide silently. → Name every transition and its pattern (delegation, creator-verifier, broadcast, negotiation).
- **Shared-state collisions.** Parallel workers write the same file, record, or codebase region with no rule for who wins. → Make the shared-state surface explicit; serialize or partition access.
- **Open loop, no budget.** The loop has no explicit stop condition, or no hard ceiling, so it runs until something external kills it. → Closed loop by default; set a max iteration count and a hard token or dollar ceiling before launch.
- **No-progress blindness.** The loop repeats without noticing it has stopped making progress – same error, same diff, same score. → Add no-progress detection as a hard stop.
- **Hopeful verification.** "Verification" is a reader that only opines, or the same context that wrote the work checking itself. → Two distinct mechanisms: an executable self-check, and an adversarial review by a fresh context that never wrote the work.
- **Missing human gate.** Irreversible or high-stakes actions run with no human checkpoint. → Place a human-review gate before each irreversible step the constraints require.
- **State held in memory.** Handoffs rely on what the previous step "remembers" rather than a written record. → Write every handoff: done / not done / commands run + exit codes / issues found.
- **Non-resumable run.** A mid-workflow failure forces a full restart because steps are not idempotent and nothing is checkpointed. → Make steps idempotent or checkpoint state to a named store, so a resume picks up where it failed rather than from zero.
- **Over-built architecture.** A solo redraft task carries an orchestrator, workers, and separate validators it does not need. → Right-size down; the smallest architecture that meets the definition of done wins.
- **Vague definition of done.** Completion is judged by feel, not by a contract that can be executed or parsed. → Write the definition of done first, in executable terms.
- **One-off prompts, no assets.** The same workflow is re-authored from scratch each time; nothing is reused or registered. → Reuse existing skills and protocols; flag recurring steps for extraction into the library.
