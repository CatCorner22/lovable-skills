---
name: rules-hygiene
description: Use when creating or trimming Lovable workspace or project Instructions, or root AGENTS.md, especially when rules grow long or conflict. Keeps durable context lean.
---

# Rules hygiene

Keep always-loaded guidance short. Put task detail where the agent can read it on demand.

## Audit the instructions
1. Read the workspace Instructions, project Instructions, and root `AGENTS.md` that are available. List any layer you cannot inspect.
2. Find duplicates, conflicts, stale commands, and task-specific runbooks.
3. Keep the top 10 lines for the most useful facts: app layout, verified build and test steps, and the 3 main risks.
4. Aim for at most 150 lines per file. Treat that as a house target, not a Lovable limit.
5. Write triggered steps: “When changing a table, check its migration and RLS.” Turn each vague or negative-only rule into a positive step with a trigger and a check: “Never break auth” becomes “When changing login code, sign in and out in the preview before you report.”
6. Move long deploy, migration, and review guides into linked project docs or skills. Verify each link.
7. Point to existing formatter, test, and security checks instead of copying their rules.
8. Add “Last reviewed: YYYY-MM-DD”. Remove stale history and repeated README text.

## Preserve the boundary
Keep safety, legal, and user-owned constraints intact. Show conflicts before resolving a material choice. Keep project-specific rules in project scope; keep workspace rules useful across projects.

Written instructions are guidance, not enforced configuration. Use actual app controls, RLS, tests, and explicit approval checkpoints for costly failures. Record which checks remain manual. Claim no automatic blocking from prose alone.

## Check
Compare old and new rules for lost meaning. Count lines, open moved references, and check that commands match the app's package scripts. Return the edited instructions, moved sections, unresolved conflicts, and checks run.
