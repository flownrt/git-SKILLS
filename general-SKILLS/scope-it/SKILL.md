---
name: scope-it
description: Turn a vague request or fuzzy idea into a concrete, structured spec in one pass – goal, scope, non-goals, and acceptance criteria – with every gap-filling assumption made explicit and the decision-critical unknowns surfaced as prioritized open questions. Generates a draft for the user to react to rather than interrogating them. Use when the user says "scope this", "turn this into a spec", "what's the spec for…", "help me define this before I start", "write a brief for…", "nail down the requirements", or hands over a vague ask they want sharpened before any work begins. Do NOT use when the requirements are already clear and the user just wants the work done, when they want to be walked through clarifying questions one at a time rather than handed a draft, or when they want a project plan or timeline rather than a definition of what "done" means. Works best with cross-examine and red-team.
---

# Scope-It

Turn a vague request or fuzzy idea into a concrete, structured spec in a single pass, and hand it over as a draft the user can react to. The job is to remove ambiguity *before* the work starts: to say plainly what is being built, what is deliberately not being built, and how everyone will know it is done.

Generate the spec yourself. Do not interrogate the user with a string of clarifying questions – fill the gaps with explicit, labelled assumptions and produce a complete draft. Where something genuinely cannot be assumed, capture it as an open question at the end rather than stopping to ask. The user gets the whole shape at once and corrects the assumptions, instead of being walked through a questionnaire.

## How to run it

1. **State the goal in one line.** Capture the underlying intent behind the request, not just its wording – what does the user actually want to be true when this is done? If the ask is broad, narrow it to the core objective worth specifying.

2. **Draft the spec.** Write it out in these parts:
   - **Goal** – the one-line objective.
   - **Scope** – what is included, concretely.
   - **Non-goals** – what is explicitly out of scope. This section is as important as Scope: it is what stops the work from sprawling.
   - **Acceptance criteria** – how you will know it is done, written so each one is checkable rather than vague. "Loads in under two seconds" beats "is fast".
   - **Constraints** – hard limits that bound the solution (deadline, budget, platform, dependencies), where any are known or can be reasonably assumed.

3. **Make every assumption explicit.** Wherever you filled a gap to keep the draft moving, mark it as an assumption in its own list, so it can be confirmed or corrected – never bury a guess inside the spec as if it were given.

4. **Surface open questions, prioritized.** List what you genuinely could not resolve. Pull the decision-critical ones – the unknowns that would change the spec if answered differently – to the top and mark them blocking. Present them as a list to answer in one go, not as questions asked one at a time.

5. **Keep it proportionate and editable.** Match the spec's weight to the task: a small ask gets a tight spec, not a template padded with empty sections. Drop any part that genuinely does not apply.

## What makes the spec good

- **Non-goals do the heavy lifting.** Most scope creep comes from what was never ruled out. Name the tempting adjacent things this is *not*.
- **Acceptance criteria are testable.** If you cannot imagine checking a criterion, rewrite it until you can.
- **Assumptions are visible, not silent.** A wrong assumption the user can see is cheap to fix; a hidden one is expensive.
- **Open questions are ranked by whether they block.** Separate the answers needed before starting from the ones that can be settled along the way.

## Output

Deliver the spec (goal, scope, non-goals, acceptance criteria, constraints), then the explicit assumptions, then the prioritized open questions with the blocking ones first. Keep it scannable and easy to edit – it is a working draft, not a finished contract.
