# study

A personal tutor that helps you learn a subject deeply across many sessions. Instead of one-shot answers, `study` builds a persistent workspace on your machine, grounds every lesson in trusted sources and your real goal, and makes you *prove* understanding before moving on – so your learning compounds instead of restarting each time.

## Recommended setup

`study` keeps its workspace as real files on disk and reads them back every session, so it works best where Claude has folder access and can persist work between sessions – **Claude Code** or **Cowork**. The tutoring, curriculum reasoning, and hand-built interactive lessons reward a strong model: **Opus 4.8** with **Max** (or at least **Medium**) reasoning is the recommended default.

## How it works

Each subject gets its own directory:

```
curricula/<subject-slug>/
  00-GOAL.md        # why you're learning this, and what success looks like
  00-RESOURCES.md   # curated trusted sources + practice communities
  00-PROFILE.md     # your preferences and the tutor's working notes
  01-lessons/       # numbered, self-contained interactive HTML lessons
  02-progress/      # short dated records of what you can now demonstrably do
  03-references/    # distilled glossaries, syntax cards, routines for quick lookup
  00-DASHBOARD.html # optional progress map of the subject (solid / developing / shaky)
```

On every session the tutor reads this state first, so a returning learner is recognized rather than re-onboarded. It teaches at your *learning edge* – the floor comes from what you've already proven (`02-progress/`), the direction from your `00-GOAL.md` – and uses spaced review to keep it from fading. Once a subject has a few progress records, the tutor can regenerate `00-DASHBOARD.html`: an at-a-glance map of every topic as solid, developing, shaky, or not started.

## Bundled starter curricula

`study` ships with three ready-made curricula in [`assets/curricula/`](./assets/curricula), built from vetted sources and deliberately different in shape:

- **[`llm-architecture.md`](./assets/curricula/llm-architecture.md)** – a three-tier *fluency map* (Mechanics → Build craft → Open debates) for understanding how large language models actually work, for someone who needs to hold their own in technical discussions. *Knowledge-heavy*: concepts to understand, each with a self-check.
- **[`chess.md`](./assets/curricula/chess.md)** – a *competency ladder* (board safety → tactics → endgames & planning) from "knows the moves" to solid intermediate. *Skills-heavy*: each rung is a thing you must be able to *do*, paired with a drill and an observable "you've got it when…" benchmark.
- **[`practical-ai.md`](./assets/curricula/practical-ai.md)** – a model-agnostic *competency ladder* for getting real work done with AI (prompt well → trust but verify → work with it → build agentic workflows). *Skills-heavy*: each rung has a "try it now" drill, and it teaches durable principles rather than today's product names.

One is a map of ideas, the other two are ladders of abilities (a classic skill, and working with AI itself) – together they show the same teaching engine handles both knowledge-led and practice-led subjects. Bring your own curriculum and it takes priority over any bundled one.

## Reference formats

The conventions the tutor follows for each workspace file live in [`references/`](./references): [`goal-format.md`](./references/goal-format.md), [`resources-format.md`](./references/resources-format.md), and [`progress-format.md`](./references/progress-format.md).

## Install

Make the skill available to Claude in one of two ways:

1. **As a folder** – copy this `study/` directory into your Claude skills directory.
2. **As a bundle** – zip the folder into a `study.skill` archive and install it through the Claude app's skill installer.

No build step is required – a skill is just `SKILL.md` (YAML frontmatter + instructions) plus the supporting files it references.

## License

Licensed under the [Apache License, Version 2.0](../LICENSE).
