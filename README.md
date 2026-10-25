<p align="center">
  <img src="assets/social-preview.png" alt="Ai Efficiency Optimizer Prompt: Save money and usage credit when using AI models" width="640">
</p>

# Ai Efficiency Optimizer Prompt

**Save money and usage credit when using AI models.**

[![License: MIT](https://img.shields.io/github/license/coreymcd37/ai-efficiency-optimizer-prompt)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last commit](https://img.shields.io/github/last-commit/coreymcd37/ai-efficiency-optimizer-prompt)](https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/commits/main)

## Contents

- [What it is](#what-it-is)
- [Why it saves money and credits](#why-it-saves-money-and-credits)
- [What's in this repo](#whats-in-this-repo)
- [Install as a skill](#install-as-a-skill)
- [Use as a system prompt](#use-as-a-system-prompt)
- [Using it with an API](#using-it-with-an-api)
- [Run the evals and scripts](#run-the-evals-and-scripts)
- [Quick mode vs. Full mode](#quick-mode-vs-full-mode)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [How this was made](#how-this-was-made)
- [Contributing](#contributing)
- [License](#license)

## What it is

I put this together because I kept burning through usage credits and paying for big models on work that didn't need them. The Ai Efficiency Optimizer Prompt is a reusable set of instructions you give an AI model so it picks the cheapest, fastest, most reliable way to get a job done, without cutting corners on accuracy, privacy, or safety.

## Why it saves money and credits

- **Right-sizes the work.** Small tasks get a quick answer, not a 3-page plan.
- **Climbs a decision ladder.** Skip it, reuse it, use free tools, or write a script before reaching for an expensive model.
- **Uses cheap models first** and only escalates hard or flagged cases to a stronger one.
- **Cuts tokens.** Shorter prompts, trimmed inputs, controlled output length, caching, and batching.
- **Caps retries and spend** so a stuck task doesn't quietly drain your credits.
- **Keeps accuracy as a hard floor,** because cheap and wrong ends up costing more.

## What's in this repo

```text
ai-efficiency-optimizer-prompt/
├── SKILL.md                  # The skill: frontmatter plus the full guide
├── CHANGELOG.md              # Version history
├── LICENSE                   # MIT
├── README.md                 # This file
├── .gitignore
├── evals/
│   ├── evals.json            # Test cases with expected and forbidden behavior
│   └── triggers.json         # Phrases that should and shouldn't trigger the skill
├── references/
│   ├── decision-ladder.md    # The 14-rung ladder, expanded
│   ├── model-tiers.md        # Choosing by capability tier, not model name
│   ├── pricing-verification.md  # How to verify and date-stamp prices
│   └── security-checklist.md # Checklist for cloud, agent, and automation setups
├── scripts/
│   ├── cost_estimate.py      # Low / expected / high cost estimator
│   └── validate_evals.py     # Checks the evals files
├── assets/
│   ├── full-mode-report-template.md  # The Full mode output skeleton
│   └── social-preview.png
├── examples/                 # Worked Quick and Full mode examples
├── prompts/
│   ├── ai-efficiency-optimizer-prompt.txt   # Plain-text copy of the guide for pasting
│   └── compact.md            # Short version for small instruction boxes
└── docs/
    └── docs-check.yml        # Optional CI workflow (see docs/README.md)
```

`SKILL.md` is the canonical guide. `prompts/ai-efficiency-optimizer-prompt.txt` is the same guide without the frontmatter.

## Install as a skill

The repo folder is the skill. Clone it into your tool's skills directory so the folder name matches the skill name, `ai-efficiency-optimizer-prompt`.

**Claude Code** (personal skills):

```bash
git clone https://github.com/coreymcd37/ai-efficiency-optimizer-prompt.git ~/.claude/skills/ai-efficiency-optimizer-prompt
```

For a single project, clone it into `.claude/skills/ai-efficiency-optimizer-prompt` inside that project instead.

**Claude apps:** download the repo as a ZIP and upload it under Settings → Capabilities → Skills.

**Cursor and other tools that read skill folders:** clone it into the tool's skills directory (for a project, typically `.cursor/skills/ai-efficiency-optimizer-prompt`). Check your tool's docs for the exact path.

The tool reads the `description` in the frontmatter to decide when to load the skill, so there's nothing else to configure.

## Use as a system prompt

1. Open [`prompts/ai-efficiency-optimizer-prompt.txt`](prompts/ai-efficiency-optimizer-prompt.txt), click **Raw**, and copy everything.
2. Paste it into your tool's standing instructions (see below).
3. Give it a real task, like "Summarize 500 support tickets by category."
4. Small jobs get Quick mode. Bigger jobs get Full mode: a recommended plan, an options comparison, cost estimates, and a small pilot before scaling.
5. Run the pilot, check the results, then scale.

Where to paste it:

- **ChatGPT:** Settings → Personalization → Custom instructions, or the instructions box of a custom GPT or Project.
- **Claude:** a Project's custom instructions, or Settings → Profile preferences for every chat.
- **Gemini:** create a Gem and paste it into the Gem's instructions.
- **GitHub Copilot:** save it as `.github/copilot-instructions.md` in your repo, or add it to your personal custom instructions.
- **Other chat apps and coding agents:** the system prompt, project rules, or instructions file.

If your tool's box is too small for the full guide, use [`prompts/compact.md`](prompts/compact.md). Menu names change from time to time, so check your tool's help pages if a setting has moved.

## Using it with an API

Send the guide as the system message, then your task as the user message. Example with an OpenAI-style chat API (swap in whichever model and SDK you use):

```python
from pathlib import Path
from openai import OpenAI

guide = Path("prompts/ai-efficiency-optimizer-prompt.txt").read_text()
client = OpenAI()  # reads your API key from the OPENAI_API_KEY environment variable

response = client.chat.completions.create(
    model="YOUR-MODEL-NAME",
    messages=[
        {"role": "system", "content": guide},
        {"role": "user", "content": "Summarize 500 support tickets by category."},
    ],
)
print(response.choices[0].message.content)
```

Tips:

- Keep the guide at the very start of the prompt so providers that support prompt caching can reuse it.
- For Anthropic's API, pass the guide in the `system` parameter. For Gemini, use `system_instruction`.
- Keep API keys in environment variables, never in code or prompts.

## Run the evals and scripts

The scripts use only the Python standard library (Python 3.8 or later).

Check the evals files:

```bash
python scripts/validate_evals.py
```

Estimate a job's cost with prices you've verified (see [references/pricing-verification.md](references/pricing-verification.md)):

```bash
python scripts/cost_estimate.py --items 2000 --input-tokens 400 --output-tokens 60 \
  --input-price 0.50 --output-price 1.50 --per 1000000
```

Run `python scripts/cost_estimate.py --help` for all options, including `--escalate` for the share of items sent to a stronger model.

To test the skill itself, run each prompt in [`evals/evals.json`](evals/evals.json) with the skill loaded and check the response against its `expected_behavior` and `must_not` lists. Use [`evals/triggers.json`](evals/triggers.json) to confirm the skill loads for the right requests and stays out of trivial ones.

## Quick mode vs. Full mode

**Quick mode** (small, low-risk task):

> **You:** Rename these 40 photos to the date they were taken.
>
> **Model:** This is deterministic, so a short script beats an AI model. Here's a 6-line script that reads each photo's date and renames it. Run it on a copy of the folder first.

**Full mode** (big, repeating, or costly job):

> **You:** Every week I get about 2,000 customer emails and need them tagged by topic and urgency.
>
> **Model:** **Recommended plan:** tag with a small, fast model and send only low-confidence emails to a stronger model, because that's the cheapest approach that meets your quality bar. Then an options table, a workflow, a low/expected/high cost estimate using `emails × tokens per email × price per token` (verify current pricing), risks, and a pilot on 50 emails before scaling.

See [`examples/`](examples/) for complete worked examples.

## FAQ

**Does it work with any model?**
Yes. It's plain instructions, so it works with any chat model or API that accepts a system prompt or custom instructions.

**Will it make answers worse?**
It shouldn't. Accuracy is a hard floor in the guide, and higher-risk work gets more checks, not fewer.

**Why doesn't it list prices or model names?**
Prices, limits, and model names change often. The guide tells the model to check official pricing pages, or to use relative ratings (Free / $ / $$ / $$$) and say "verify current pricing".

**It's too long for my tool's instructions box.**
Use [`prompts/compact.md`](prompts/compact.md).

**Can I change it for my team or company?**
Yes. It's MIT licensed. Fork it, trim it, and adapt it.

## Roadmap

- [ ] Setup guides for more tools and coding agents
- [ ] Model-specific tips
- [ ] More worked examples
- [ ] Translations

Have an idea? [Open an issue](https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/issues/new/choose) or start a [discussion](https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/discussions).

## How this was made

I developed and tested this guide through my own AI-assisted workflow. I wrote the rules, tested them on real tasks, and kept only what held up. It's the same approach I use when I build software: I set the direction, review every result and ship what passes.

— [Corey McDaniel](https://coreymcdaniel.com)

## Contributing

This is meant to grow. If you have a better rung for the ladder, a token-saving trick, a tool-specific setup guide, or a fix, I'd love your help. Open an issue, start a discussion, or send a pull request. Everyone's welcome to build on it, collaborate, and contribute. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started, and look for issues labelled [`good first issue`](https://github.com/coreymcd37/ai-efficiency-optimizer-prompt/labels/good%20first%20issue).

## License

[MIT](LICENSE) © 2026 Corey McDaniel
