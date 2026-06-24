---
name: improve-prompt
description: Rewrite an existing prompt that is rough, sprawling, or underperforming into a stronger, copy-pasteable version – pulling the real task to the front, supplying the role, context, output format and constraints the model needs, resolving contradictions, and flagging the gaps only the user can fill – then briefly explain what changed. Works on a pasted draft prompt, a system prompt, or an agent instruction. Use when the user says "improve this prompt", "make this prompt better", "rewrite this prompt", "optimize my prompt", "why isn't this prompt working", "clean up this prompt", or pastes instructions for an AI and wants them sharpened. Do NOT use to run the prompt or produce its output, to teach prompt engineering as a lesson, to interrogate the user one question at a time, to turn a blank brief or a pile of requirements into a spec (that is scoping, not prompt improvement), or for image-generation / diffusion prompts.
---

# Improve-Prompt

Take an existing prompt that is rough, sprawling, or underperforming and rewrite it into the strongest version of what its author was reaching for. The work is subtraction as much as addition: pull the buried task to the front, fill the structural gaps, resolve the contradictions, and cut whatever pulls the model off course. A longer prompt is not a better one.

Deliver a finished rewrite in a single pass. Do not interrogate the user. Missing facts – a name, a number, a policy, a document – become clearly marked placeholders in the rewrite, never questions. Ask at most one question, and only when the prompt's *goal* is so ambiguous that any rewrite would be a coin-flip; a merely missing detail is never a reason to ask.

## How to run it

1. **Pin the intent and the target use.** Work out what the prompt is actually for, where it runs (a single chat turn, a system prompt, a reusable agent instruction), and what a good result looks like. Everything downstream serves that goal; rewriting the words without it just produces polished noise.

2. **Diagnose, then rewrite.** Find the specific weaknesses – a buried or compound task, missing role or context, no output format or length, self-contradictory or negative-only instructions, detail pitched at the wrong level – and fix each one. State the task plainly up front, supply the context the model cannot infer, spell out the output format and length, turn "don't do X" into "do Y", and separate instructions from data with sections or tags once the prompt grows complex. Apply only what this prompt needs – an over-engineered prompt is its own failure.

3. **Preserve intent; mark what you can't know.** Improve how the prompt asks, not what it asks for – do not expand the task, shift the goal, or substitute your own preferences. Where the prompt depends on something only the user knows, leave a labelled placeholder rather than inventing a value, and call out separately any gap that is *risky to guess wrong* so the user fixes it before shipping.

4. **Match and name the level of intervention.** A light polish when the prompt is mostly sound; a full restructure when it is not. Say which you did, and offer the opposite as a one-line option the user can take – never make them compare two versions they did not ask for.

## Hold the line on quality

This is what separates a real improvement from a reflexive reword:

- **Fix the prompt, don't pad it.** Length is not improvement. If a change does not make the model's job clearer, cut it.
- **Preserve intent.** A rewrite that quietly changes what the user asked for is a failure, however polished the result.
- **Make guesses visible.** A placeholder the user can see is cheap to correct; an invented detail buried in the rewrite is expensive – and the gaps that are dangerous to get wrong are the ones to flag loudest.
- **Earn every technique.** Examples, role framing, step-by-step scaffolding, and tags all cost length and rigidity – use them where they pay off, not by reflex.

## Output

Deliver, in order: the rewritten prompt in a single copy-pasteable block – a fenced code block when it is a reusable system or agent prompt; then a brief "what changed and why", each point tied to a weakness you found and proportionate to the prompt rather than an essay; then the placeholders and assumptions the user must still fill, with any guess-at-your-peril gaps marked loudest. Close with a one-line offer of the opposite level of intervention – lighter or more aggressive – when it would be reasonable.
