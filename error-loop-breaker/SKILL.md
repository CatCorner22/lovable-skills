---
name: error-loop-breaker
description: Use when the same error comes back after a fix, when a fix breaks something else, when Try to fix has failed twice, or when the user says it keeps breaking or is stuck in a loop. Stops blind retries and finds the root cause before more code is written.
---

# Error-loop breaker

Repeated blind fixes pile up code that hides the real problem. Stop, find the cause, then fix it once.

## Step 1. Stop
Do not change more code yet. Count the failed fixes. After 2, stay in this skill until Step 4.

## Step 2. Collect the evidence
- The exact error text, from the console, network, and backend logs.
- The last version that worked, and what changed since then.
- What the user did, what they expected, and what happened.

## Step 3. Find the root cause (read-only)
Use subagents to look at the problem from different angles in parallel:
- What the error trace points to.
- What the diff since the last working version changed.
- Data, permission, or setting causes: row-level security, missing secrets, a schema mismatch, or an expired session.

State the root cause in 1 sentence, with the file and line. If you cannot, say what evidence is still missing and get it.

## Step 4. Choose a path
| Situation | Path |
|---|---|
| Cause found, code still clean | Make 1 small fix aimed at the cause. |
| Earlier fixes have tangled the code | Revert to the last working version, then apply the 1 fix. |
| Error is in login, payments, or personal data | Revert first. Plan the fix before writing it. |

## Step 5. Prove it
Rerun the exact steps that failed. Check that nearby flows still work. Remove patches the earlier failed fixes left behind.
