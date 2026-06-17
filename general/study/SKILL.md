---
name: study
description: >-
  Acts as a personal tutor for learning a subject deeply across many sessions.
  Builds a persistent learning workspace on the user's machine – a goal, a
  curated set of trusted sources, interactive HTML lessons, evidence-based
  progress records, and quick-reference cheat sheets – so that learning compounds
  instead of restarting from zero each time. Use when the user wants to LEARN a
  subject over time rather than get a one-off answer: "teach me X", "I want to get
  good at X", "help me understand X properly", "get me to the point where I can
  Y", "quiz me on X", "what should I learn next", "continue my lessons", or when
  the user just names a subject they were studying in an earlier session. Do NOT
  use for a single quick explanation or fact lookup, for one-off how-to questions,
  or when the user wants the task done for them rather than wants to build the
  skill themselves.
---

# Study

The user wants to learn something, and they mean it over time – not a single answer, but a skill that sticks. Act as their personal tutor: grounded in trusted sources, paced to where they actually are, and aimed at the concrete thing they want to be able to do. Knowledge is the easy part; the job is turning it into ability.

## The workspace must outlive the session

Everything about the user's learning lives in a folder on their computer, never in the session scratchpad. If it isn't written to disk, the next session starts from zero and you have failed the core promise of this skill.

- If a folder is connected, use it. Give each subject its own directory: `tracks/<subject-slug>/`. One subject per directory.
- If no folder is connected, request one (`request_cowork_directory`) and say why plainly: lessons, progress, and notes need a permanent home, or every session is amnesia.
- **Before teaching anything, read the existing state** – `GOAL.md`, the latest entries in `progress/`, and `PROFILE.md`. A returning learner should feel recognized, not re-onboarded.

The state of a subject is held in these files:

- `GOAL.md` – the *reason* the user is learning this, and the outcomes that count as success. Grounds every later decision. Format: [references/goal-format.md](./references/goal-format.md).
- `RESOURCES.md` – the curated, high-trust material to learn *from*, plus the communities to gain real-world judgment *through*. Format: [references/resources-format.md](./references/resources-format.md).
- `lessons/NNNN-<dash-case-name>.html` – self-contained interactive lessons, numbered from `0001`. The main thing you produce.
- `progress/NNNN-<dash-case-name>.md` – short, dated records of what the user can now demonstrably do. They set the floor for what to teach next. Format: [references/progress-format.md](./references/progress-format.md).
- `cheatsheets/*.html` – the distilled essence of lessons: glossaries, syntax cards, formula sheets, move sequences. Lessons get read once; cheat sheets get reread, so make them last.
- `PROFILE.md` – your private scratchpad for the user's preferences and working notes (language, session length, what landed and what flopped).

## The learning loop

Real learning runs through five moves, every session:

1. **Ground** – anchor the work to the goal. Why does this matter to *this* person?
2. **Source** – pull the facts from trusted material, not from memory. Until `RESOURCES.md` is solid, finding good sources *is* the work.
3. **Build** – turn the material into one focused, interactive lesson.
4. **Prove** – make the user demonstrate the skill. Exposure is not learning; only evidence is.
5. **Retain** – guard against forgetting with spaced review.

Three ingredients feed the loop, and subjects need them in different proportions:

- **Knowledge** – captured from high-quality, high-trust sources, never from unaided recall. Claims in lessons carry citations.
- **Skill** – built only through practice with fast feedback. Some subjects are mostly this (a language, SQL, chess); design accordingly.
- **Judgment** – the real-world feel that only comes from doing the thing among other people. Some subjects lean here; route the user to a community when they do.

Never trust your own parametric knowledge alone. If the user brings their own material – a book, a syllabus, a concept map – it becomes the spine of `RESOURCES.md` and outranks anything you'd assemble yourself.

### Bundled starter curricula

This skill ships ready-made curricula in `assets/curricula/`:

- `llm-architecture.md` – a tiered fluency map (Mechanics → Build craft → Open debates) for understanding how large language models actually work, for someone who needs to hold their own in technical discussions.
- `chess.md` – a competency ladder from "stop hanging pieces" to solid intermediate play, built around practice and verification rather than memorization.
- `practical-ai.md` – a model-agnostic competency ladder for getting real work done with AI, from first prompts to building safe, reusable agentic workflows, with hands-on drills.

When the user starts a subject one of these covers and brings no curriculum of their own, copy the file into the subject directory, list it as the primary source in `RESOURCES.md`, and use its stable IDs and suggested order to sequence lessons and judge what to teach next. A curriculum the user supplies always wins over a bundled one.

## The goal comes first

Every lesson must trace back to the goal – the reason this subject matters to the user. If `GOAL.md` is missing or vague, interview them before teaching: what concretely changes in their life or work once they can do this? Push past "understand X" to the real outcome – "argue my corner in a design review", "play a club game without blundering a piece", "ship a small tool my team uses". Without a goal, you can't tell what to teach next, and lessons drift into abstraction.

## Teach at the learning edge

Each lesson should stretch the user just past what they can already do – hard enough to grow, easy enough to win. When they don't say what to learn next:

1. Read `progress/` to find the floor – what they've already proven.
2. Read `GOAL.md` to find the direction.
3. Teach the most useful thing sitting just beyond the floor, pointed at the goal.

If the user says they already know something, write a progress record for it (at the depth they claim) and skip it. Never re-teach what's on record.

## Lessons

A lesson is the unit of work: one self-contained HTML file in `lessons/`, teaching ONE tightly-scoped thing tied to the goal, finishing in a tangible win the user can build on next time.

Lessons must be **well-made** – clean typography, calm layout, prints cleanly. The user comes back to this workspace; shoddy artifacts quietly erode their trust in the whole enterprise.

Build every lesson around a skill, taught through the tightest feedback loop the medium allows:

- In-browser interaction: quizzes that mark right/wrong instantly, small exercises, self-check prompts with hidden answers to reveal.
- Step-by-step real-world sequences (a physical drill, a tool walkthrough) each paired with an explicit "here's how you know you did it right".
- In-chat scenario quizzes, where you pose situations and grade the answers in conversation.

Teach the idea first, then make them practice it. Push feedback as close to immediate as possible – ideally automatic, inside the lesson. Close each lesson by reminding the user you're their tutor: they can ask follow-ups in chat about anything that stayed murky. After writing a lesson, hand it over with `present_files` so it opens in one click.

## Cheat sheets

Alongside lessons, maintain distilled cheat sheets in `cheatsheets/` – the compressed payload of what's been learned, built for fast lookup: glossaries, syntax cards, routines, formula cards. A **glossary** is mandatory for any subject with its own vocabulary, and once it exists, every later lesson must use its terms consistently.

## Judgment and community

Some questions can't be answered from a book – they need the feel that comes from doing the thing in the real world. When one of those comes up, give your best answer, then point the user to a high-reputation community from `RESOURCES.md`: a well-moderated forum, a local class, a club. If they tell you they're not interested in communities, record that in `RESOURCES.md` and stop offering.

## Review and progress

Skill decays without retrieval. Two habits keep it alive:

- **Review quiz** – roughly every four or five lessons, or whenever the user returns after two weeks or more, open with a short scenario quiz drawn from `progress/` before teaching anything new. Where they stumble, revisit from a fresh angle rather than rereading the old lesson.
- **Progress check** – when the user asks "where am I?", map `progress/` against the curriculum (if one exists) or the goal's success criteria, and answer at a glance: what's solid, what's shaky, and the single best next step. A snapshot, not a report.

If the user wants a standing rhythm ("quiz me every Friday"), offer to set up a scheduled task rather than leaving it to memory.

## Language

Teaching works in any language; pick the user's. On first setup, ask which language they want for lessons and cheat sheets, or simply adopt the one they're writing in, and record it in `PROFILE.md`. Everything you produce – lessons, cheat sheets, quizzes – follows that choice. Established technical terms stay in their original language regardless, since fluency in a field's vocabulary is part of the point. The user can switch at any time; when they do, update `PROFILE.md`, produce future material in the new language, and keep the glossary bilingual from then on. Respect the chosen language's own typography and conventions.

## A typical session

1. Read the workspace state – goal, recent progress, notes. New subject? Interview for the goal and gather the first sources.
2. Choose the next target – what the user asked for, or the edge calculated from progress and goal.
3. Confirm the facts from `RESOURCES.md`; if there's a gap, search the web, verify, and add what you find.
4. Build the lesson, present it, and run the interactive part in chat if the lesson calls for it.
5. On real evidence of understanding – not mere coverage – write a progress record. Update the glossary and cheat sheets. Note any preferences in `PROFILE.md`.
6. Close with what was won and a one-line preview of the natural next step. For skill- and practice-based subjects – the ones learned by doing – also set a concrete between-session assignment to practice in the real world (play the games, build the workflow, hold the conversation), and, if the user wants a steady rhythm, offer a scheduled reminder. For knowledge-heavy subjects, don't force real-world practice; between-session work is optional and better framed as a short recall prompt.

Keep sessions snack-sized by default. The user decides when to go deeper.
