---
name: claim-evidence-pairing
description: Use when writing a factual report, diagnosis, research summary, or numerical claim about the app. Attaches sources and confidence to decision-critical claims. Not for proof that a task is complete → use completion-evidence-gate; not for testing the user's premise → use premise-check.
---

# Claim–evidence pairing

Give the reader a way to check each claim that affects a decision.

## 1. Find the claims
Mark numbers, dates, versions, causes, and claims that “the code does X”. Leave taste and style judgments as judgments.

## 2. Pair the evidence
Use this compact form:

`Claim [src: file:line, URL, or check | "short exact quote" | confidence: probable]`

Keep each quote at 30 words or fewer. Quote raw output when it is the evidence. Explain it after the quote. Link to the actual source, not a search result or a guessed citation.

## 3. Set confidence
- **Established:** an official source and independent confirmation agree.
- **Probable:** 1 strong source supports the claim; no known contradiction.
- **Contested:** sources disagree. State how.
- **Single-source:** 1 report makes the claim; you have not verified it.
- **Unknown:** the checks found no answer. List what you searched.

Match the wording to the label: “is” for established, “appears” for probable, and “the report says” for single-source.

For a diagnosis, show the failing symptom, the path that runs, and the cause. Test an alternative explanation. Mark any missing link unverified.

## 4. Keep a record
For a long report, keep a short claims table in project files: claim, source, quote, confidence, date, and open check. Update it when the code or source changes.

Check that every cited file and URL exists and supports the exact claim. Preserve uncertainty and conflicting evidence when shortening the report. Unknown is a useful result.
