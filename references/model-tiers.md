# Model Tiers

The guide says: don't hardcode model names; pick by capability tier and check what's currently available. Model names and line-ups change often, so this reference describes tiers by what they're good for, not by name.

## The three tiers

| Tier | Typical strengths | Typical trade-offs | Good fit |
|---|---|---|---|
| **Small / fast** | Low cost per token, quick responses, good at well-defined tasks | Weaker on multi-step reasoning and subtle judgment | Classification, extraction, formatting, summarizing, simple translation, cleaning, first drafts |
| **Mid** | Solid general reasoning at moderate cost | Can still miss edge cases on hard problems | Most everyday writing, analysis, and coding tasks |
| **Frontier** | Strongest reasoning, long and complex instructions, hard code | Highest cost and often slower | Hard reasoning, high-stakes review, flagged cases the smaller tiers couldn't handle |

Local or open-source models can fall into any tier. They're worth considering when data is sensitive, volume is large, or ongoing cost matters, but be honest about hardware and setup effort.

## Choosing a tier

1. Start with the smallest tier that could plausibly meet the quality bar.
2. Run a pilot on 5-10 items and measure quality.
3. Escalate only the cases that fail or are flagged as low confidence (cheap-first, escalate-when-needed).
4. Use the frontier tier directly only when reasoning is hard or errors are costly.

## Finding what's available

- Check the provider's current model list in its official documentation.
- Check which models your plan or account can use.
- Verify each model's price on the official pricing page (see [pricing-verification.md](pricing-verification.md)).

## Mixing tiers in one workflow

A single job can use several tiers: a small model for bulk extraction, a mid model to draft, and a frontier model or a person to review flagged or high-risk items. Keep a separate verifier for high-risk work.
