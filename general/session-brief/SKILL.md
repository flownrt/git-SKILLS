---
name: session-brief
description: Distills the current session into a self-contained continuation prompt – a copy-pasteable brief that lets a fresh session resume the work without re-explaining it. Reads the thread for what a follow-up session actually needs (topic, goal, current state, must-reads in order, decisions already made, open questions, pause points, out-of-scope, success indicator) and outputs the brief as a fenced markdown block in the chat. Use when the user wants to hand the current work off to a new session: "session brief", "continuation prompt", "pack this into a brief", "I'll pick this up in a fresh chat", "save where we are so I can continue later", or at the end of a long, unfinished thread. Do NOT use when the task finishes in this session, or when a couple of sentences would do – write that short note instead of a full brief.
---

# Session Brief

A session brief is a self-contained continuation prompt: everything a fresh session needs to resume the work, and nothing it doesn't. One shot – distill it from the thread, don't iterate.

## How to run it

1. **Read the session for these axes** – whatever is missing here is missing from the brief:
   - **Topic** – one line: what the work is.
   - **Goal** – the outcome the next session aims at, plus the intended mode, skill, or approach if it matters.
   - **Current state** – where things stand now.
   - **Must-reads** – files, docs, or links to read first, in order (cap ~8); a repo's conventions file comes first.
   - **Decisions made** – settled choices with a one-line reason each, so they aren't reopened.
   - **Open questions** – what's unresolved, numbered, in a single block.
   - **Pause points** – where the next session must stop for approval.
   - **Out of scope** – what it should explicitly NOT do.
   - **Success indicator** – how it knows it's done.

2. **Floor-check.** If this fits in three bullets, holds no real decisions yet, or would just restate the obvious – skip the brief and give a short handoff note inline instead.

3. **Write the brief as a fenced markdown code block** so the user can copy it 1:1 into a fresh session. Inside: a header (topic + date), one to three sentences of situation anchor, then the axes above that apply, and a **first step** to take. Capture the session's working process only if one was actually established – don't invent one.

4. **Output inline by default**, in one code fence. Save to a file only if asked (`session-brief-<slug>.md` in the user's folder); assume no particular repo layout exists.

5. **Report back** in a line or two. If the goal or mode was ambiguous, pick the likeliest reading and say so.

## Keep in, leave out

Keep what a fresh session can't reconstruct: decisions, must-reads in order, open questions, pause points, out-of-scope, success indicator. Leave out generic tool reminders, background rationale the follow-up doesn't need to act on, and conventions already written in the project's files – point to them, don't copy them.

## Avoid

- A brief with no copy-pasteable block – the block is the deliverable.
- Splitting open questions across several places instead of one numbered block.
