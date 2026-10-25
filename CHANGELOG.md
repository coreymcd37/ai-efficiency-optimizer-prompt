# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

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

[1.1.0]: https://github.com/coreymcd37/ai-efficiency-optimizer/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/coreymcd37/ai-efficiency-optimizer/releases/tag/v1.0.0
