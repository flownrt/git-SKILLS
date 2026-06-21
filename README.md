# git-SKILLS

A curated, public collection of Agent Skills I use every day, for personal and professional work. A skill is a small `SKILL.md` (plus any files it references) that teaches an agent how to do one thing well – the agent loads it automatically when your request matches, or you can call it by name.

Every skill here is self-contained, model-agnostic, and general-purpose by design: useful straight out of the box and easy to build on.

## Skills

Grouped by category; each category's README indexes the skills inside it.

- [`general-SKILLS/`](./general-SKILLS) – domain-agnostic skills.
- [`legal-SKILLS/`](./legal-SKILLS) – legal workflows.

## Setup

These skills work with any agent that supports Agent Skills, especially Claude Code and Cowork. There's no build step.

**1. From the marketplace (recommended).** One managed install that stays updated. Add it once, then pull in any skill by name:

```
/plugin marketplace add flownrt/git-SKILLS
/plugin install study@git-skills
```

Every skill installs the same way (`<name>@git-skills`); run `/plugin` to browse and manage them interactively. Update with `/plugin marketplace update git-skills`.

Without commands:

- **Cowork** – add it from the UI – Customize → Personal plugins → + → Create plugin → Add marketplace, then enter this repo.
- **Claude Code** – declare it in `settings.json`, which also turns on `autoUpdate` so skills refresh at startup (third-party marketplaces are off by default):

```json
{
  "extraKnownMarketplaces": {
    "git-skills": { "source": { "source": "github", "repo": "flownrt/git-SKILLS" }, "autoUpdate": true }
  },
  "enabledPlugins": { "study@git-skills": true }
}
```

**2. By hand.** Clone the repo (`git clone …`) or download the ZIP, then:

- **Cowork** – download a skill's prebuilt bundle (`<skill>.skill`) from the [latest release](https://github.com/flownrt/git-SKILLS/releases/latest), then Customize → Personal plugins → + → Create plugin → Upload plugin. (Or build it yourself: `cd general-SKILLS && zip -r study.skill study`.)
- **Claude Code** – copy a skill's folder into `~/.claude/skills/` (every project) or a project's `.claude/skills/` (that project only). Picked up the same session, no restart.

Once installed, the agent triggers a skill automatically when your request matches its description, or you can invoke it by name.

## License

Licensed under the [Apache License, Version 2.0](./LICENSE); see [`NOTICE`](./NOTICE) for attribution.
