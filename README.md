# Smart Efficiency Optimizer

**Save Money and Usage Credit When Using AI Models**

I put this together because I kept burning through usage credits and paying for big models on work that didn't need them. The Smart Efficiency Optimizer is a reusable set of instructions you give an AI model so it picks the cheapest, fastest, most reliable way to get a job done, without cutting corners on accuracy, privacy, or safety.

## Why it saves money and credits

- **Right-sizes the work.** Small tasks get a quick answer, not a 3-page plan.
- **Climbs a decision ladder.** Skip it, reuse it, use free tools, or write a script before reaching for an expensive model.
- **Uses cheap models first** and only escalates hard or flagged cases to a stronger one.
- **Cuts tokens.** Shorter prompts, trimmed inputs, controlled output length, caching, and batching.
- **Caps retries and spend** so a stuck task doesn't quietly drain your credits.
- **Keeps accuracy as a hard floor,** because cheap and wrong ends up costing more.

## How to use it

Copy the contents of [`SMART-EFFICIENCY-OPTIMIZER.md`](SMART-EFFICIENCY-OPTIMIZER.md) into whichever slot your tool gives you for standing instructions:

- **ChatGPT:** Custom Instructions, or the instructions box of a custom GPT or Project
- **Other chat apps:** Project instructions, system prompt, or "custom instructions" setting
- **APIs:** use it as the `system` message
- **Coding tools and agents:** put it in the project rules or instructions file

## Quick start

1. Open [`SMART-EFFICIENCY-OPTIMIZER.md`](SMART-EFFICIENCY-OPTIMIZER.md) and copy everything.
2. Paste it into your AI tool's system prompt or custom instructions.
3. Give it a real task, like "Summarize 500 support tickets by category."
4. Small jobs get Quick mode. Bigger jobs get Full mode: a recommended plan, an options comparison, cost estimates, and a small pilot before scaling.
5. Run the pilot, check the results, then scale.

## Contributing

This is meant to grow. If you have a better rung for the ladder, a token-saving trick, a tool-specific setup guide, or a fix, I'd love your help. Open an issue, start a discussion, or send a pull request. Everyone's welcome to build on it, collaborate, and contribute. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## License

[MIT](LICENSE) © 2026 Corey McDaniel
