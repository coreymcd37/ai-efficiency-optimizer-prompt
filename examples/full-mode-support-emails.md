# Full mode: tagging support emails

> Illustrative example. Not a benchmark. Costs use relative ratings; verify current pricing before relying on any estimate.

**Task**

> Every week we get about 2,000 customer emails. I need each one tagged by topic (billing, shipping, product, other) and urgency (low, normal, urgent).

**Assumptions:** emails are in a shared inbox you can export to CSV; a few wrong tags are acceptable if urgent emails are rarely missed.

## 1. Recommended plan

Tag every email with a small, fast model using structured JSON output, and send only low-confidence or "urgent" emails to a stronger model for a second look. It's the cheapest approach that meets your quality bar.

## 2. Options compared

- **Do it directly (a person tags them):** Free in tools, $$$ in time. Accurate but slow.
- **Inbox rules and keyword filters:** Free. Fast, but misses anything worded unusually. Good for a first pass on obvious billing and shipping emails.
- **Small model for everything:** $. Good for topic, weaker on subtle urgency.
- **Small model + stronger model for flagged cases (recommended):** $ to $$. Strong accuracy where it matters.
- **Stronger model for everything:** $$$. Little accuracy gain over the recommended option.

## 3. Workflow

1. Export the week's emails to CSV (you).
2. Strip signatures and quoted replies to trim tokens (script).
3. Batch emails into one request per 20 emails; ask for JSON with `topic`, `urgency`, `confidence` (small model).
4. Validate the JSON in code; re-send any malformed rows once (script).
5. Send rows with `confidence < 0.7` or `urgency = urgent` to the stronger model (stronger model).
6. Spot-check 10% of the results by hand (you).

## 4. Cost and time estimate

Plug-in formula: `emails × tokens per email × price per token`, plus the same for the flagged share on the stronger model.

- **Low:** few flagged emails, short messages.
- **Expected:** about 10-20% flagged.
- **High:** long threads, many flagged.

Guardrails: monthly spend cap and alert at 80%, max 2 retries per batch, kill switch if the flagged share goes above 40%.

## 5. Risks and safeguards

- **Privacy:** customer emails contain personal data. Check the provider's data retention and training terms first, and remove card numbers and addresses before sending.
- **Accuracy:** missed urgent emails are the costly failure, so urgent tags always get a second check.
- **Fallback:** if the API is down, inbox rules still catch the obvious cases.

## 6. Quick win

Run the pipeline on 50 past emails you've already tagged by hand. Compare the results and measure the actual cost before scaling.

## 7. Scale-up path

If volume grows a lot, the break-even point may favor a local open-source model for the first pass. Re-check once the weekly cost is known.
