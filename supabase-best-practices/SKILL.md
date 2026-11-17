---
name: supabase-best-practices
description: Use when writing or tuning Supabase schema, migrations, SQL, indexes, edge functions, auth, or storage code for a Lovable app. Combines safe data design with measured query work. Not for proving cross-user isolation → use rls-leak-check; not for Stripe billing flows → use payments-stripe-safe.
---

# Supabase best practices

Check current Supabase docs before using an API or security feature. Read the app's existing migrations and backend setup first. Use the backend access Lovable provides; name any missing access rather than invent a tool.

## 1. Model and migrate
Choose explicit owners and tenant keys. Use primary keys, foreign keys, unique constraints, suitable types, defaults, and checks for invariants. Add indexes for real filters, joins, foreign-key lookups, and policy predicates. Keep migrations reviewable and versioned.

Rehearse with example data in a draft or test backend. Plan backfill, compatibility, locks, backup, and recovery before a live migration. Verify the resulting schema and data. Keep production changes within approved scope.

## 2. Design access
Enable RLS on every table in an exposed schema. Match policies to real roles and operations. Check Data API exposure and grants separately from row policies. A missing grant and a denied policy are different faults.

Use publishable keys in public clients. Keep service-role and secret keys in backend secrets. Verify caller identity in edge functions before privileged work. Derive owner IDs from verified identity, not request data.

Use trusted role data, not user-editable `user_metadata`, for authorization. Remember that JWT claims can stay stale until refresh. User deletion does not itself revoke issued access tokens; use a current, verified session/revocation design for sensitive operations.

Use security-invoker views where supported, or restrict view access. Keep security-definer helpers in unexposed schemas, with a safe search path, narrow grants, and explicit checks. UPDATE also needs a matching SELECT policy.

Use private storage unless public access serves the product. Scope object paths and policies to ownership. Storage upsert needs INSERT, SELECT, and UPDATE rights.

Run `rls-leak-check` for cross-user, signed-out, and role-escalation proof. Built-in quick or deep security scans complement those tests; they do not replace them.

## 3. Measure queries
Use [references/query-checks.md](references/query-checks.md) for slow queries, large tables, pooling, and concurrency. Inspect plans before and after. Select needed columns, bound result sets, paginate with a stable order, and batch repeated work.

## 4. Keep functions safe
Validate input, authenticate callers, limit work, handle timeouts, and return safe errors. Keep secrets and personal data out of logs. Make retried writes idempotent. Put atomic multi-row changes inside a transaction or database function.

## 5. Verify and report
Test success, empty results, invalid input, denied access, and backend failure. Check persisted rows and storage behavior. Report migrations, policy intent, query evidence, and limits. After 2 failed approaches, inspect docs and the actual error; use `error-loop-breaker` for a stuck repair.
