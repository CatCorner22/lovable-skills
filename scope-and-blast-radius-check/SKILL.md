---
name: scope-and-blast-radius-check
description: Use when a proposed delete, overwrite, migration, deployment, or other risky action could affect data or systems outside the intended change. Resolves targets and rollback first. Not for the overall publish checklist → use launch-gate; not for repository sync conflicts → use github-sync-guard.
---

# Scope and blast-radius check

Resolve the target before changing it. A draft uses example data; it does not prove a live migration is safe.

## Before the action
1. State the allowed files, project, backend, environment, and action. Read existing permissions before asking again.
2. Resolve each path, wildcard, project ID, database connection, bucket, and deployment target. Show names without secret values.
3. List what the action changes, who it affects, and what depends on it. Include auth, billing, data, and integrations.
4. Classify the action. A code edit with a usable revert is reversible. Data loss, production cutover, outward publication, and history rewrites need explicit approval if the user has not already approved that exact scope.
5. Prepare all safe work first. Show the target, effect, backup, restore check, and exact proposed action. Ask for a go-ahead on the remaining risky step.

Use a draft or test environment for rehearsal. Verify the target again at execution time. Resolve any test/live ambiguity before writing.

## After the action
Read back the result. Inspect the changed files, affected row count, bucket contents, or deployed version. Check a nearby flow that shares the changed resource. Record the count or result.

If the target differs from the plan, stop and report it. Keep the boundary narrow rather than widening it to bypass a failure.

## Rollback
Name the owner, trigger, and recovery steps. Version history helps restore code. Use a separate, tested data backup and restore plan for database changes. A frontend revert alone does not restore records.

Return scope, target, risk class, approval when needed, result, and remaining limits. These written steps guide the agent; they do not create an automatic safety block.
