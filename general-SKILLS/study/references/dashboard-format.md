# Dashboard format (`00-DASHBOARD.html`)

`00-DASHBOARD.html` is the rendered projection of the curriculum (`04-resources/<subject-slug>.md`) – the one screen that answers "where am I?" at a glance. It is strictly derived: it never shows a concept the curriculum doesn't, and a subject too trivial for a curriculum gets no dashboard. Build it with `assets/workspace-styles.css` and the subject's single accent, like every other artifact, and regenerate it from the curriculum whenever you write a progress record.

## Required anatomy, top to bottom

1. **Overall-progress summary – always first, never omitted.** The headline the user scans before anything else: a large **percent complete**, the **weighted concept count** ("24.1 of 36 concepts"), the **tally** by state (solid / developing / shaky / not started), and a **pill row** of those four states. This block is mandatory on every dashboard. A dashboard that opens straight into the goal or the concept rows, with no overall figure, is incomplete – it is the single most common thing to get wrong.
2. **Goal** – the goal restated in one line (`.goal` / `.callout`), so progress is read against the point of it.
3. **Provenance note** – one line: that the map is projected from `04-resources/<subject-slug>.md`, the rule that a concept only turns *solid* on real evidence (a chat answer or real-world result, not a read lesson), and an **Updated YYYY-MM-DD** date.
4. **Floor & next step** – what's proven (the floor) and the single next concept; link the delivered-but-unproven lesson if one is pending.
5. **Concept rows, grouped by curriculum tier** – one `.dash .row` per concept: the concept ID in `.cid` (accent) then its short label · `.meter` · state pill, in curriculum order. Use the shared `.dash .row` grid as-is – its name column is sized to hold a short label without wrapping; don't roll a bespoke grid or a custom ID class.

## The four states (fixed)

Each concept is in exactly one state, shown by its pill and meter fill, and carrying a weight that feeds the overall percent:

| State | Pill · meter fill | Meter width | Weight | Meaning |
| --- | --- | --- | --- | --- |
| Solid | `p-solid` · `fill-good` (green) | 100% | 1.0 | proven on the benchmark's verb, by real evidence |
| Developing | `p-dev` · `fill-acc` (accent) | 60% | 0.6 | taught and practised, not yet proven |
| Shaky | `p-shaky` · `fill-warn` (amber) | 30% | 0.3 | proven once, then stumbled on review |
| Not started | `p-none` · `fill-none` (neutral) | 0% | 0 | not yet taught |

**Overall percent = (Σ weights) ÷ (concept count), rounded.** Example: 19 solid + 7 developing + 3 shaky + 7 not-started over 36 concepts → (19 + 4.2 + 0.9) ÷ 36 = 24.1 / 36 = **67%**. Always show the weighted count next to the percent, so the number is legible rather than magic.

## Rules

- **Lead with the summary.** The overall-progress block is non-negotiable and comes first. Everything below it is detail.
- **Strictly derived.** Every concept on the dashboard exists in the curriculum, by the same stable ID and in the same order. Re-seed from the curriculum whenever it changes; never hand-place a concept the curriculum doesn't have.
- **Solid means proven.** Only real evidence – a chat answer or a reported real-world result – turns a concept solid, never a delivered-but-unproven lesson. A lesson handed over but awaiting evidence is *developing*, with its pending marker in `00-PROFILE.md`.
- **One accent, fixed semantics.** Same accent as the rest of the subject; the green / amber state colours never change with it.
- **A snapshot, not a report.** Summary, goal, next step, the map – all on a glance. If it reads like prose, it has stopped being a dashboard. It prints cleanly; the user returns to it.
