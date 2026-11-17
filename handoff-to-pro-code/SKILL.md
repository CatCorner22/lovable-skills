---
name: handoff-to-pro-code
description: Use when moving an app out of Lovable to a developer-owned codebase, Supabase project, and frontend host. Covers export, migration, cutover, and rollback. Not for day-to-day two-way repository sync → use github-sync-guard.
---

# Handoff to pro code

Move in stages. Keep the old app working until the new stack passes the same checks.

## 1. Freeze a baseline
Record the current version, domain, routes, backend project, auth providers, storage buckets, edge functions, integrations, and known issues. Use `github-sync-guard` to settle sync direction before export. Sync to GitHub and download the codebase as a separate backup. Verify that both contain the expected files.

Keep root `AGENTS.md`. Update it with setup, build, test, backend, secret names, and release steps. Keep secret values in the target's secret store. Record dependencies and the lockfile.

## 2. Plan backend migration
Use current Supabase and Lovable export guidance. Confirm which exports and access the current backend permits. State blockers rather than promise a 1-click move.

Write a checklist with owner, source, target, check, and rollback for:
- Schema, migrations, extensions, indexes, triggers, views, functions, grants, and RLS.
- Data, row counts, foreign keys, timestamps, and a plan for writes during cutover.
- Auth users and IDs, identities, providers, redirects, email templates, and password migration support. Verify the supported transfer method; plan reauthentication or reset if sessions or passwords cannot move safely.
- Storage files, paths, metadata, bucket settings, and policies. Check counts and file access.
- Edge functions, schedules or integrations the app actually uses, and secret names and values through secure transfer.

Test with example data first. Rehearse on a separate target. Protect real user exports and remove temporary copies under the agreed retention plan.

## 3. Deploy and cut over
Identify Vite or TanStack Start from the code. Match its build, server runtime, routes, and environment setup on the new frontend host. Point it at the new Supabase project. Test login, refresh, permissions, data writes, uploads, functions, billing, and deep links.

Agree on the write freeze or delta-transfer method. Take final backups. Get approval for production changes. Switch URLs, auth redirects, webhook targets, and domain settings in a recorded order. Watch errors and compare key counts and flows.

## 4. Keep rollback usable
Define failure triggers, decision owner, and rollback window before cutover. Preserve the old deployment and backend. Explain how new writes will return to the old backend; a frontend revert alone cannot restore data. Rehearse restoration. Retire old services only after approval and a verified backup.

Return the code location, migration checklist, proof, unresolved items, and rollback steps.
