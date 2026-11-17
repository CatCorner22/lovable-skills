---
name: red-team-review
description: Use when the user says red team, attack this, break this, stress test, or pre-mortem, or before launching an app that handles logins, payments, or personal data. Runs independent attacker subagents against the app the user owns, then a separate judge subagent that confirms or rejects each finding. Every confirmed finding gets a fix and a retest.
---

# Red-team review

Try to break the app before real users or attackers do. The attackers try to win. A separate judge decides what is real.

## Rules
1. Attack only this project and its own backend. Never attack other sites, other people's data, or live customer accounts.
2. Work in a draft when one is available, so tests use example data, not live records.
3. Attackers do not grade their own work. A separate judge subagent does.
4. Write every finding down before anyone defends the code. Never delete a confirmed finding. Close it only with a fix and a passing retest.
5. Show only enough of an attack to prove it. Never paste a live secret into a finding.

## Step 1. Set the target (1 short note)
- The question, in 1 sentence. Example: "Can a signed-in user read or change another user's data?"
- The surfaces: pages, forms, backend functions, database tables, storage buckets, webhooks, AI prompts, and roles.

## Step 2. Run attacker subagents in parallel (read-only)
Use subagents. Start 1 per lane. Each lane gets only its own goal.

| Lane | Attacker goal |
|---|---|
| Data thief | Read or change rows that belong to someone else. Check row-level security on every table and every storage bucket. |
| Role climber | Do admin or paid-only actions as a normal or free user. Call backend functions directly, skipping the screen. |
| Money breaker | Get the product without paying, pay twice, or replay a webhook. Change prices or amounts in the browser. |
| Input abuser | Send bad, huge, empty, or script-laden input to every form, URL parameter, and backend function. |
| Secret hunter | Find secret keys, tokens, or private URLs in client code, logs, or network responses. |
| Prompt injector | If the app uses AI, make it reveal its instructions, leak other users' data, or take actions it should not. |
| Chaos user | Double-click, go back, refresh mid-flow, lose the network, and use 2 tabs at once. Look for broken state. |

Each finding states: lane, steps to reproduce, what happened, what should happen, and severity (critical, high, medium, low).

## Step 3. Judge (separate subagent)
- Reproduce each finding from its steps. If it does not reproduce, mark it "not confirmed" and give the reason.
- Grade strictly. A false alarm costs more than a missed low-severity issue.
- Rank confirmed findings by severity.

## Step 4. Fix and retest
1. Fix critical and high findings first, 1 at a time.
2. Rerun that finding's exact steps. It must now fail for the attacker.
3. Rerun the lane once more to catch side effects.
4. Report a table: finding, severity, status (fixed and retested, accepted risk, open), and proof.

The review is done only when every critical and high finding is fixed and retested, or the user accepts the risk in writing.
