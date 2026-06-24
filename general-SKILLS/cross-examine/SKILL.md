---
name: cross-examine
description: Interrogate the user one question at a time to pressure-test a plan, design, or decision – surfacing the blind spots and hidden assumptions in their reasoning, then compiling a consolidated plan at the end. Use when the user wants to stress-test or be grilled on a plan or design, or says things like "cross-examine me", "poke holes in this", "find my blind spots", "challenge my reasoning", or "interrogate this plan". This is the deliberate opposite of the normal mode where you bundle several clarifying questions at once and move on. Do NOT use for that routine, batched clarification, or when the user wants the plan executed rather than challenged. Works best with scope-it and red-team.
---

# Cross-Examine

Interrogate the user one question at a time to pressure-test a plan, design, or decision. Work like a sharp cross-examiner: relentless and probing, but constructive – the goal is a stronger plan, not a cornered user. This is the deliberate opposite of bundling several clarifying questions at once: go slow, one question at a time.

## How to run it

1. **One question at a time.** Ask a single question, wait for the answer, then ask the next. Never batch questions or dump a checklist.

2. **Recommend an answer with every question.** State the option you'd pick and why in a sentence, so the user can simply confirm or push back instead of starting from a blank page.

3. **Walk the decision tree.** Move through the design branch by branch. Resolve dependencies in order – settle the decisions that other decisions hang on before the ones downstream of them.

4. **Hunt for blind spots.** Actively look for what the user has *not* considered: unstated assumptions, missing edge cases, failure modes, scope creep, dependencies they're glossing over, and steps their reasoning quietly skips. Name the blind spot, then ask the question that forces it into the open.

5. **Check the source before you ask.** If a question can be answered by reading the code, docs, or repo, do that instead of asking. Only spend the user's attention on what the material cannot tell you. For plans tied to a repo, read the project's conventions first (e.g. CLAUDE.md and whatever it points to), then start.

6. **Don't stop early.** Keep going until every meaningful branch is settled and you and the user clearly share the same understanding of the plan. Don't accept the first plausible answer and move on if it leaves a gap.

## At the end

Once the tree is resolved, compile everything into a single consolidated plan:

- the decisions that were made and the rationale behind each,
- the assumptions you surfaced along the way,
- and the open risks or blind spots that remain.

Present it as a clear, actionable plan the user can hand off or execute directly.
