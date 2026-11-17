# Lovable skills

25 custom skills for Lovable, in the Agent Skills `SKILL.md` format.

Descriptions guide skill selection. Each skill keeps a narrow job; use its boundary notes to pick the right one.

## Lovable workflow

| Skill | Use it for |
|---|---|
| four-lens-build | Any multi-file change: 4 read-only subagents (the end, the beginning, the big picture, each line), then small slices checked as they are built. |
| error-loop-breaker | Stops blind "Try to fix" loops and finds the root cause. |
| credit-saver | Picks the cheapest mode and groups small edits. |
| feature-spec | Questions first, then a 1-screen spec with done-when tests. |
| github-sync-guard | Keeps Lovable and outside tools from overwriting each other. |
| ask-or-assume | Resolves small information gaps with focused questions or labeled assumptions. |
| premise-check | Checks a stated fact or diagnosis before building on it. |
| rules-hygiene | Keeps workspace/project Instructions and root AGENTS.md lean. |
| negative-constraint-compiler | Turns vague warnings into positive, testable steps. |
| handoff-to-pro-code | Moves code, backend, and hosting out of Lovable with a rollback plan. |

## Quality and review

| Skill | Use it for |
|---|---|
| red-team-review | Attacker subagents plus a separate judge for an app attack. |
| rls-leak-check | Cross-user and signed-out data-access tests that scans can miss. |
| launch-gate | One go or no-go review before publishing. |
| completion-evidence-gate | Matches completion claims to checks and actual results. |
| claim-evidence-pairing | Gives factual claims sources and clear confidence labels. |
| scope-and-blast-radius-check | Resolves risky targets, approval, backups, and recovery. |
| chicken-little-overwatch | Audits AI-written documents for meaning, evidence, and writing quality. |

## Writing

| Skill | Use it for |
|---|---|
| plain-copy | Makes app text, transactional emails, and onboarding clear and brief. |
| adams-policy-drafting | Drafts privacy, terms, consent, and refund pages for lawyer review. |
| smart-brevity | Shapes executive updates and briefs with the key point first. |

## Backend and code

| Skill | Use it for |
|---|---|
| evidence-based-ui-design | Chooses visual direction and tokens, then checks rendered screens. |
| ux-engineering | Repairs task flows, forms, feedback, and recovery states. |
| stable-architecture | Keeps domain rules testable and adapters replaceable. |
| supabase-best-practices | Guides schema, migrations, RLS design, indexes, functions, auth, and storage. |
| payments-stripe-safe | Builds server-owned Stripe billing with test-mode proof. |

## Install
Workspace settings → Skills → Add → Upload ZIP, one ZIP per skill. Or Import from GitHub with the skill's folder URL (public repos only).

Run `python3 validate_skills.py` after edits to check Lovable's limits.

`dist/` contains 1 ZIP per skill and `lovable-skills-all.zip`, the full library with this README and the validator. Use individual ZIPs for skill uploads. The validator runs outside Lovable; skills use written checks, not bundled scripts.

Supporting Markdown files load only when a skill links to them. Lovable subagents are read-only; the main agent makes edits. Drafts use example data. Version history restores code, not a database backup. Built-in security scans and SEO/accessibility skills complement these skills.
