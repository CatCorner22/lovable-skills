---
name: four-lens-build
description: Use when building or changing any feature, page, backend function, or data model, and the work touches more than one file. Plans the change through 4 lenses at once with read-only subagents (the end, the beginning, the big picture, each line of code), then builds it in small slices that are checked before the next slice starts. Not for one-line copy or style tweaks.
---

# Four-lens build

Build it right the first time. Do not write a full plan, build it all, and then debug for days.
Look at the work through 4 lenses before you code. Check each small slice as you write it.

## Step 1. Run the 4 lenses in parallel (no code yet)

Use subagents. Start 4 read-only subagents at the same time. Give each one only its own question.
Each one must return a short note: findings, file paths, and risks. No code changes.

| Lens | Question the subagent answers | It returns |
|---|---|---|
| A. The end | What does "done" look like to the user? Work backward from that to the first line of code. | Done-when tests a user could run. The backward chain: outcome → screens → actions → data → backend → schema → first file. |
| B. The beginning | In what order must the code be written so each step only uses things that already exist? | A numbered build order. Any step that needs something from a later step. |
| C. The big picture | Will this hold up at 100 times today's users and data? | Risks in the data model, indexes, row-level security, pagination, repeated queries, caching, server rendering, cost per user, and tight coupling. The fix for each. |
| D. Each line | What rules must every line in this project follow? | The project's conventions, types, and existing helpers to reuse. The lean-code rules in [references/lean-code.md](references/lean-code.md) that apply. |

## Step 2. Join the lenses into one plan

1. Lay chain A (backward) beside order B (forward). They must meet. A gap or a mismatch is a hole in the plan. Fix it now.
2. Apply every C risk that matters at launch. List the rest as "later" with the reason.
3. Cut the work into thin slices. Each slice:
   - changes as few files as it can,
   - leaves the app working,
   - has 1 check that proves it works.
4. Show the plan as a short table: slice, files, check. Wait for approval if the user is in Plan mode.

## Step 3. Build one slice, then check it, then move on

For each slice, in order:

1. Write the slice. Follow lens D's rules. Reuse what exists. Add nothing the slice does not need.
2. Check it right away:
   - The build passes with no type errors.
   - The preview loads with no console errors.
   - The slice's own check passes (click the flow, test the query, call the function).
3. Review the diff with a fresh read-only subagent using lens D. Fix what it finds now.
4. Every 3 slices, or after any data or backend change, rerun lens C on the new code.
   - For a slice the customer sees, run `voice-of-customer` on it before you move on.
5. Go to the next slice only when every check passes.

Stop rule: if the same slice fails twice, stop writing code. Find the root cause first (read the error, the logs, and the diff). Revert the slice if the fix gets tangled. Then try again with a smaller slice.

## Step 4. Close out

1. Run every done-when test from lens A.
2. Delete dead code, unused imports, debug logs, and leftover files.
3. Report in this shape:
   - Done: what now works, in user terms.
   - Checked: each check and its result.
   - Later: deferred lens C items and why.

## Limits to know

- Subagents in Lovable are read-only. They look and report. Only the main agent writes code.
- Lovable decides when to start subagents. Saying "use subagents" asks for them. If none start, run the 4 lenses yourself in order A, B, C, D, and keep each one's note separate.
- For risky data changes, build in a draft so the work runs on example data, not live records.
