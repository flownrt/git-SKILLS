# git-SKILLS

Agent Skills I use every day – for personal and professional work. Each one is self-contained and model-agnostic: general-purpose by design – useful straight out of the box, and easy to build on.

## Setup

These skills work with any agent that supports Agent Skills, especially Claude Code and Cowork. A skill is just a `SKILL.md` plus the files it references – there's no build step.

1. **One-click install (Claude Code & Cowork)** – add this repo as a plugin marketplace, then install any skill by name:
   ```
   /plugin marketplace add flownrt/git-SKILLS
   /plugin install study@git-skills
   ```
   `cross-examine` and `session-brief` install the same way. Refresh later with `/plugin marketplace update git-skills`. (Add the marketplace via the Git repo, as above, so the bundled skill files resolve.)
2. **Or install by hand** – clone the repo (`git clone …`) or download the ZIP, then:
   - **Claude Code** – copy a skill's folder into `~/.claude/skills/` (every project) or a project's `.claude/skills/` (that project only). Picked up the same session, no restart.
   - **Cowork** – zip the skill's folder, then add the archive under Settings → Capabilities:
     ```
     cd general-SKILLS && zip -r study.skill study
     ```
3. **Use it** – the agent triggers a skill automatically when your request matches its description, or you can invoke it by name.

## Skills

Grouped by category; each category's README indexes the skills inside it.

- [`general-SKILLS/`](./general-SKILLS) – broadly useful, domain-agnostic skills.
- [`legal-SKILLS/`](./legal-SKILLS) – legal workflows.

## License

Licensed under the [Apache License, Version 2.0](./LICENSE); see [`NOTICE`](./NOTICE) for attribution.
