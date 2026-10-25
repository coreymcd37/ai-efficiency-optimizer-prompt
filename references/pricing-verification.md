# Pricing Verification

Prices, rate limits, free tiers, and model names change often. The guide's rule is simple: **verify prices and limits; never invent them.** This reference explains how.

## Where to look

1. **The provider's official pricing page.** Go to the provider's own website, not a blog post, reseller, or comparison site.
2. **The provider's official documentation** for rate limits, context limits, batch discounts, and caching rules. These are often on a different page from prices.
3. **Your own account's billing or usage page.** It shows what you are actually being charged, including any plan, region, or contract differences.

Third-party comparison sites can help you find options, but confirm every figure on the official page before using it.

## What to record

For each price you use, record:

- The provider and the exact product or tier name as shown on the page
- The unit (per request, per 1,000 tokens, per 1M tokens, per minute, per month)
- Input and output prices separately, if they differ
- Any discounts that apply (batch, cached input, committed use) and their conditions
- Free-tier limits and whether free-tier inputs may be used for training
- The URL and the date you checked it

## Date-stamp template

Copy this into your plan next to any figure you quote:

```text
Source: [provider] official pricing page, [URL]
Checked: [YYYY-MM-DD]
Item: [product or tier name]
Unit: [per 1M input tokens / per request / per month]
Price: [amount and currency, as shown on the page]
Conditions: [batch, cache, region, plan, or volume terms]
```

## When you can't verify

If you have no way to check the official page:

- Use relative ratings: **Free / $ / $$ / $$$**.
- Say "verify current pricing" next to every estimate.
- Give the plug-in formula instead of a number: `items × tokens per item × price per token`.
- Never state a specific price from memory as fact.

## Running the numbers

Once you have verified prices, use [`scripts/cost_estimate.py`](../scripts/cost_estimate.py) to get low, expected, and high estimates. The script never supplies prices itself; you pass in the figures you verified.
