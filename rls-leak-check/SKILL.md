---
name: rls-leak-check
description: Use when adding or changing a database table, storage bucket, or backend function, when the user asks about data security, or before publishing. Checks that every row and file is readable and writable only by the right users, which the built-in security scans can miss.
---

# Row-level security leak check

The built-in scans flag tables with security turned off. They can miss rules that are on but let everyone in.

## Step 1. List every table and bucket
For each one, write: who owns a row, who may read it, who may write it, and whether it is public on purpose.

## Step 2. Check each rule against that list
Flag a rule as a leak when it:
- uses `using (true)` or `with check (true)` on data that is not public,
- only checks `auth.uid() is not null`, so any signed-in user can see every row,
- covers SELECT but not INSERT, UPDATE, or DELETE (or the reverse),
- lets a user set `user_id`, `role`, `org_id`, or `price` to any value on insert or update,
- joins to another table that has no rule of its own,
- sits on a view or function that skips row-level security (`security definer` without its own checks).

## Step 3. Check the code around the database
- No service-role or other secret key in client code. Only the public key goes to the browser.
- Every backend function checks who the caller is before it reads or writes data.
- Storage buckets are private unless the files are meant to be public.

## Step 4. Prove it with 2 test users
In a draft or with test accounts, sign in as user A and user B. Confirm that:
1. A cannot read, change, or delete B's rows or files.
2. A signed-out visitor gets nothing from private tables.
3. A normal user cannot change their own role or plan.

## Step 5. Fix and report
Write the missing or tighter rules. Rerun Step 4. Report a table: table or bucket, the problem, the fix, and the test result.
