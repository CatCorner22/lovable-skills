---
name: negative-constraint-compiler
description: Use when a negative or vague rule in Lovable Instructions, AGENTS.md, or SKILL.md needs a positive, testable step, or when the agent missed a written rule. Not for trimming the whole instruction set → use rules-hygiene; not for executing risky changes → use scope-and-blast-radius-check.
---

# Negative constraint compiler

Turn a warning into an action with a clear trigger and observable result.

## For each rule
1. Name the harm the rule prevents. Preserve its scope and exceptions.
2. Write: “When <trigger>, do <positive action>; check <observable result>.”
3. State what happens if the check fails: stop, repair, ask, or use a safe fallback.
4. Decide the control layer. Keep a cheap style check as prose. For a failure that could cost data or more than 10 minutes, add a concrete test, app control, RLS policy, or approval checkpoint.
5. Keep a short pointer to the control in the instructions. Record any manual step.

## Examples
| Intent | Positive step |
|---|---|
| Keep secrets out of the browser | Before adding a key, store secret values in backend secrets; inspect client imports and public environment variables. |
| Keep tenants apart | Before exposing a table, enable scoped policies; test access as 2 users with rls-leak-check. |
| Keep live data safe | Before a migration, identify the backend and backup; rehearse with example data and get approval for live changes. |
| Keep edits in scope | Before writing a file, compare its path and purpose with the agreed file list. |

## Review
Check that each rule has a trigger, action, result, and failure path. Replace “be careful” and “as appropriate” with a named check. Compare the rewrite with the source for meaning.

Lovable does not gain runtime enforcement from a written rule. Label written gates as manual. Use the app's real controls for security. Keep necessary prohibitions alongside the positive step when law or policy needs their exact wording.

Return a table: source rule, new step, control, evidence, and remaining gap.
