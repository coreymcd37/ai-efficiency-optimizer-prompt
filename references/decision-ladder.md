# Decision Ladder

An expanded walk through Step 2 of [SKILL.md](../SKILL.md). Work down the ladder and **stop at the first option that meets the quality bar.**

| # | Rung | Ask yourself | Choose it when |
|---|---|---|---|
| 1 | Don't do it / simplify | Is this needed? Is there a 20% effort that gives 80% of the value? | The result isn't worth the effort, or a simpler version is enough |
| 2 | Reuse what exists | Is there a template, file, script, saved prompt, or checklist already? | Something close already exists |
| 3 | Free or already-owned tools | Can a spreadsheet formula, find-and-replace, email filter, or OS automation do it? | The tool is already available and fits |
| 4 | Do it directly | Can one well-written prompt handle it? | It's a single, bounded task |
| 5 | Smaller or cheaper model | Is the work simple, repetitive, and low-risk? | Classification, extraction, formatting, summarizing, cleaning |
| 6 | Stronger model | Is reasoning hard or are errors costly? | Only for the hard or flagged cases |
| 7 | Code instead of AI | Is the task deterministic? | Sorting, math, patterns, renaming, format conversion, scheduled jobs |
| 8 | Local or open-source model | Is data sensitive, volume large, or ongoing cost a concern? | Quality is good enough and setup is realistic |
| 9 | Automation or no-code tools | Does the process repeat? | A trigger-and-action flow covers it |
| 10 | Existing software or SaaS | Does buying beat building? | Total cost (subscription, setup, switching, lock-in) is lower |
| 11 | Cloud or serverless | Is there bursty compute, storage, queues, or hosting? | Needed, with budget caps and alerts on |
| 12 | Multiple agents | Does the work split into independent parallel pieces or distinct specialist roles? | Not for sequential, simple, or tightly coupled work |
| 13 | People | Is human judgment, presence, licensing, or a relationship required? | The user's time is worth more than the fee |
| 14 | Licensed professional | Is it legal, medical, tax, safety-critical, or regulated? | The downside is severe |

## Common mistakes

- **Skipping rungs 1-3.** The cheapest step is the one you skip, and free tools are often already on hand.
- **Using AI for deterministic work.** Use AI to write the script once, then run it free (rung 7).
- **Starting with the strongest model.** Start small and escalate only what needs it (rungs 5-6).
- **Reaching for multiple agents too early.** Few agents, narrow jobs, small contexts, and a separate verifier, and only when work truly splits (rung 12).
- **DIY on regulated work.** When the downside is severe, cheapest-correct is not DIY (rung 14).

## Example

Renaming 40 photos by date: rung 7 (code instead of AI) applies, so a short script beats any model. See [examples/quick-mode-renaming-photos.md](../examples/quick-mode-renaming-photos.md).
