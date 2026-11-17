---
name: completion-evidence-gate
description: Use when preparing a completion or status report that claims work is done, fixed, implemented, or passing. Pairs each acceptance test with actual evidence. Not for the publish decision → use launch-gate.
---

# Completion evidence gate

Match each success claim to a check you actually ran.

## 1. Compare the work with the goal
Read the request and done-when tests. List each acceptance item and the changed files. Mark each item complete, partial, blocked, or unchecked.

## 2. Collect fresh proof
Run the smallest check that answers each item. Use build or type checks for code validity. Exercise the app flow for behavior. Inspect saved rows for persistence. Use a rendered view for visual claims.

A page that loads does not prove that its form saves. A screenshot does not prove RLS. A version revert does not prove that a data migration rolled back.

Use the checks Lovable makes available. If execution or backend access is missing, name the missing check and report it as not run. Keep a proposed check separate from an observed result.

## 3. Report
Use this block for each group of acceptance items:

```
Acceptance: what counts as done
Check: exact command or app actions, role, and environment
Output: "verbatim result" or a precise observed result with artifact location
Diff: changed files and their purpose
Not verified: remaining behavior, platforms, or data states
```

Quote output with counts or error lines when available. For a manual flow, state what you entered and what changed. Cite only evidence from this run and current version.

Say “partial — 2 of 3 criteria met” when that is the result. Keep failed checks visible. Replace predictions with “not run” or a bounded claim. Read the final diff for unrelated changes before reporting.
