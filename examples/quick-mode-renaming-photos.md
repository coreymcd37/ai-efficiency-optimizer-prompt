# Quick mode: renaming photos

> Illustrative example. Not a benchmark.

**Task**

> I have 40 vacation photos named IMG_0001.jpg and so on. Rename them to the date they were taken.

**Response**

This is deterministic, so a short script is cheaper and more reliable than asking a model to do it. Run this in the folder (it uses the free `exiftool` utility). Test it on a copy of the folder first:

```bash
exiftool '-FileName<DateTimeOriginal' -d '%Y-%m-%d_%H%M%S%%-c.%%e' .
```

Photos taken in the same second get a `-1`, `-2` suffix so nothing is overwritten.

**Why this is Quick mode:** under 10 minutes, low risk, one obvious approach. No tables or plan needed.
