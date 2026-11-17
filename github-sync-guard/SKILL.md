---
name: github-sync-guard
description: Use when the project is connected to GitHub, when someone also edits the code in Cursor, Claude Code, Devin, or another tool, or when the user mentions branches, merge conflicts, or lost changes. Keeps Lovable and outside edits from overwriting each other.
---

# GitHub sync guard

Lovable syncs both ways with GitHub, but it edits and syncs 1 branch at a time.

## Rules
1. Check which branch Lovable is set to before you change code. Say it in your reply.
2. Outside tools work on their own branches and merge into the Lovable branch through a pull request.
3. Pull in outside changes before a large edit. Do not start a big change while an outside branch is about to merge.

## Keep a root AGENTS.md
Lovable always reads a root `AGENTS.md`. Keep it under 100 lines and shared by every tool:
- Stack and how to run, build, and test.
- Folder map: where pages, components, backend functions, and migrations live.
- Coding rules: point to the lean-code rules.
- Things to never touch by hand, such as generated types or the Supabase client file.

## After a sync
- Confirm the build passes on the synced code.
- If outside edits changed the database schema, confirm the migrations match the live tables.
- Report any file that both sides changed.
