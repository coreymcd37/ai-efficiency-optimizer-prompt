# Lesson: Spell out your output format

> A real lesson from testing the prompt, in my own words.

## What happened

When I was testing this, I noticed I still needed to be more specific about the output format when it mattered to me (and it did). The most cost-effective, efficient path the agent figured out wasn't necessarily what I wanted, or a format I could actually use.

Here's my example. I needed a usable file I could open like normal, a PDF or a text file. Instead, the bot put the output into an account it uses through an MCP connection, because that gave instant output and was ultimately cheaper. When I went to get the file, I needed login details, and neither I nor the bot had them. That account was something set up through skills and connected services. So I had to convert the output again, which turned into yet another task, and that cost more and used more credits than just doing it my way the first time.

## The takeaway

Explain exactly what you're doing and what you need as the output, then let the bot figure out the most efficient way to get it to you. Put the emphasis on the absolutes, like the file extension or the place the file has to go. Those are the things that can't be compromised on.

The cheapest path only counts if the result lands in a form and a place you can actually use.

## Before and after

**Before** (leaves the output open to interpretation):

```text
Summarize these meeting notes into a report for me.
```

**After** (states the non-negotiables up front):

```text
Summarize these meeting notes into a one-page report.

Output requirements (non-negotiable):
- File type: PDF
- Delivery: attach it here in this chat so I can download it directly
- Access: I must be able to open it without logging in to any other account or service

Use whatever is most efficient to produce it, as long as those three are met.
```

## Why this saves money

A result you can't open isn't done. Converting or re-delivering it is a second task, and that usually costs more than getting the format right the first time. Stating your file type, destination, and access needs up front keeps the efficient path pointed at something you can use.
