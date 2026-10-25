# Full Mode Report Template

The output skeleton from Step 5 of [SKILL.md](../SKILL.md). Copy it and fill in each section for the job at hand. Keep it short and skimmable, and lead with the recommendation.

```markdown
# [Task name]: Efficiency plan

**Assumptions:** [one line]

## 1. Recommended plan

Do [X] using [Y] because it's the cheapest approach that meets your quality bar.

## 2. Options compared

| Option | How it works | Cost | Time | Accuracy | Privacy/Risk | Effort | Best when |
|---|---|---|---|---|---|---|---|
| Do it directly | | | | | | | |
| [Option 2] | | | | | | | |
| [Option 3] | | | | | | | |

Costs use relative ratings (Free / $ / $$ / $$$) unless verified with a date and source.
Formula: `items × tokens per item × price per token`

## 3. Workflow

1. [Step]: [who or what does it] → [input] → [output] ([check])
2. [Step]: ...

## 4. Cost and time estimate

| | Low | Expected | High |
|---|---|---|---|
| Cost | | | |
| Time | | | |

**Key assumptions:** ...
**Guardrails:** spend cap [ ], alert threshold [ ], retry limit [ ], kill switch [ ]

## 5. Risks and safeguards

- **Privacy:**
- **Accuracy:**
- **Lock-in:**
- **Failure points and fallback:**

## 6. Quick win

[A 10-minute pilot on 5-10 items to measure quality and cost.]

## 7. Scale-up path

[How to extend it, and the break-even point where a different approach becomes cheaper.]
```

On small screens, replace the options table with a short list of the 2-3 most relevant options.
