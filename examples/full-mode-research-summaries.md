# Full mode: summarizing research papers with sensitive notes

> Illustrative example. Not a benchmark. Costs use relative ratings; verify current pricing before relying on any estimate.

**Task**

> I have 120 PDFs of research papers plus my own confidential notes on each. I want a one-paragraph summary per paper and a short list of themes across all of them.

**Questions (only ones that change the plan):** Can the notes leave your computer? How accurate does each summary need to be?

**Assumptions (if no answer):** the notes are confidential and stay local; summaries are for your own reading, so medium risk.

## 1. Recommended plan

Extract the text from each PDF with a free tool, summarize the papers (public content) with a small cloud model, and handle your confidential notes with a local model only. It keeps your notes private and the cloud cost low.

## 2. Options compared

- **Do it directly (read and summarize yourself):** Free, $$$ in time.
- **Paste everything into a chat app:** $. Fast, but sends confidential notes to a third party. Not recommended without your OK.
- **Small cloud model on papers + local model on notes (recommended):** $. Private and cheap; some setup effort.
- **Local model for everything:** Free after setup. Needs a capable computer and is slower.

## 3. Workflow

1. Extract text from each PDF with a free command-line tool (script).
2. Send only the abstract, introduction, and conclusion of each paper to cut tokens (script).
3. Summarize each paper in one paragraph, in batches (small cloud model).
4. Summarize your notes locally (local model).
5. Combine the 120 short summaries and ask for cross-cutting themes (one request, mid-tier model).
6. Spot-check 12 summaries (10%) against the papers (you).

## 4. Cost and time estimate

Formula: `papers × tokens per trimmed paper × price per token`, plus one themes request. Low / expected / high depends mostly on paper length. Set a spend cap before starting.

## 5. Risks and safeguards

- **Privacy:** notes never leave your computer.
- **Accuracy:** summaries can miss nuance; flag any that disagree with your notes.
- **Licenses:** only process papers you have legitimate access to.

## 6. Quick win

Try the full workflow on 5 papers and check the summaries before running all 120.

## 7. Scale-up path

If you'll repeat this monthly, save the scripts and prompts as a reusable template.
