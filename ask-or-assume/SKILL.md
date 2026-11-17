---
name: ask-or-assume
description: Use when a small task has an information gap or the agent is about to interrupt with a question. Classifies gaps and labels cheap assumptions. Not for scoping a whole new feature → use feature-spec; not for validating a stated diagnosis → use premise-check.
---

# Ask or assume

Ask about choices the user owns. Read what the app can tell you.

## Classify each gap
| Gap | Action |
|---|---|
| Goal: who benefits or what outcome matters | Ask before work. Batch related questions. |
| Input: which file or value applies | Inspect code and project context first. Ask if evidence cannot settle an expensive choice. |
| Constraint: what may change | Use existing instructions and permissions. Label a cheap, reversible assumption. Confirm risky scope changes. |
| Context: how a module works | Read callers, tests, and current configuration. |

## Decide
1. List the missing facts and try the cheapest direct checks.
2. Ask when 2 readings change product behavior, legal effect, cost, or data risk.
3. Proceed when a wrong guess is cheap to undo. Write “Assumed: …” near the choice and in the closeout.
4. Give a focused question with options and a reasoned recommendation. Group all open questions in 1 message.
5. For irreversible actions, use `scope-and-blast-radius-check`.

## Keep work moving
Aim for at most 1 interruption per phase: plan, build, verify. After the midpoint, finish with labeled reversible assumptions unless a real blocker or material risk appears. This is a timing guide, not a reason to hide a new safety issue.

Keep a short list of decisions and assumptions in the plan. Reuse answers already given. Separate a request for a user-owned decision from a request for information available in the code.

Return the result and any assumptions that still matter. For a new feature with several goal gaps, switch to `feature-spec`.
