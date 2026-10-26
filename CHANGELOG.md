# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [1.2.1] - 2026-10-26

### Changed

- Regenerated `prompts/compact.md` from the v1.2.0 guide. It now includes strict output discipline, truthfulness, the workaround protocol, and the output rules, including treating file type, destination, and access as hard constraints.

## [1.2.0] - 2026-10-25

### Changed

- `SKILL.md` now holds the second version of the guide. It's tighter and more direct, and several sections are condensed into short rule lists.
- Core principle 4 now covers model capabilities as well as prices and limits.
- Core principle 6 now says to state trade-offs only when they affect the decision.
- Step 3 is condensed into one paragraph and adds "stop as soon as the requested result is complete."
- Step 5 now includes only the sections the task requires.
- Step 6 gives a retrospective only when asked, and offers a reusable template only when relevant.
- The red flags, security checklist, and accuracy controls are condensed. The longer versions are still in `references/`.
- `prompts/ai-efficiency-optimizer-prompt.txt` is synced with the new guide.

### Added

- **Strict output discipline:** deliver only what was asked for; fuller output only on explicit request.
- **Truthfulness rules:** no fabricated facts, sources, prices, capabilities, or results; constructed workarounds must be labelled as such.
- **Workaround protocol:** instead of refusing outright, find the legitimate goal and the closest legal, safe alternative, never by bypassing access controls.
- **Output rules**, including treating stated output requirements (file type, destination, access) as hard constraints.
- A red flag for generating unrequested content that consumes credits.
- `examples/lesson-specify-output-format.md`: a lesson from real testing on spelling out output requirements, with a before/after prompt.
- A "Notes from testing" section in the README.
- An eval case for output format as a hard constraint.

### Removed

- The separate "Tone" section; its intent is covered by the new output discipline and output rules.

## [1.1.1] - 2026-10-25

### Changed

- Renamed the project to **Ai Efficiency Optimizer Prompt**. The repository is now `coreymcd37/ai-efficiency-optimizer-prompt`; old links redirect automatically.
- The skill name in `SKILL.md` is now `ai-efficiency-optimizer-prompt`, so install it into a folder with that name.
- `prompts/ai-efficiency-optimizer.txt` is now `prompts/ai-efficiency-optimizer-prompt.txt`.
- Updated the title and links across the README, guide, templates, references, and social preview image. The guide's wording is unchanged.

## [1.1.0] - 2026-10-25

### Changed

- Renamed the project from Smart Efficiency Optimizer to **Ai Efficiency Optimizer**. The repository is now `coreymcd37/ai-efficiency-optimizer`; old links redirect automatically.
- Restructured the repository into the standard agent-skill layout, so the folder can be dropped straight into a skills directory.
- `SMART-EFFICIENCY-OPTIMIZER.md` is now `SKILL.md`, with YAML frontmatter (`name`, `description`, `version`, `author`, `license`). The guide's wording is unchanged.
- `prompts/smart-efficiency-optimizer.txt` is now `prompts/ai-efficiency-optimizer.txt` and stays in sync with `SKILL.md`.
- Moved the social preview image to `assets/social-preview.png`.
- Rewrote the README with a file tree and install steps for skill folders, system prompts, and the evals.

### Added

- `evals/evals.json`: seven test cases covering Quick mode, Full mode, the privacy red flag, unverified pricing, paywall and terms-of-service bypass, multi-agent overuse, and trivial tasks.
- `evals/triggers.json`: phrases that should and should not trigger the skill.
- `references/`: pricing verification, model tiers, decision ladder, and security checklist.
- `scripts/cost_estimate.py`: a dependency-free low / expected / high cost estimator that uses prices you supply.
- `scripts/validate_evals.py`: checks the evals and trigger files for schema and minimum counts.
- `assets/full-mode-report-template.md`: the Full mode output skeleton.
- `.gitignore`.

## [1.0.0] - 2026-10-24

### Added

- The full Smart Efficiency Optimizer guide (`SMART-EFFICIENCY-OPTIMIZER.md`).
- A plain-text copy for easy pasting (`prompts/smart-efficiency-optimizer.txt`).
- A compact version for tools with small instruction limits (`prompts/compact.md`).
- Worked examples of Quick mode and Full mode (`examples/`).
- Setup instructions for ChatGPT, Claude, Gemini, GitHub Copilot, and APIs.
- Contributing guide, code of conduct, security policy, support guide, and issue and pull request templates.

[1.2.1]: https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/releases/tag/v1.0.0
