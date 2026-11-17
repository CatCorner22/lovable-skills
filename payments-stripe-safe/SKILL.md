---
name: payments-stripe-safe
description: Use when adding or changing Stripe checkout, subscriptions, webhooks, refunds, or cancellation in a Lovable app. Covers server-side billing and test-mode proof. Not for general database design → use supabase-best-practices; not for access-leak testing → use rls-leak-check.
---

# Payments: Stripe safe

Treat Stripe as the billing source of truth. Treat browser values as untrusted.

## 1. Map the flow
List products, currencies, server-approved price IDs, user-to-customer mapping, plan access, refunds, and cancellation timing. Confirm current Stripe API guidance. Keep test and live environments separate.

Store test and live secret keys and webhook signing secrets only in backend secrets. Use a publishable key in the browser only if Stripe's client flow needs it; it is public, not a secret. Keep every secret key out of Vite variables, client code, logs, and version history.

## 2. Build the server boundary
1. Create Checkout Sessions in an edge function. Verify the caller and derive the customer from their account.
2. Resolve prices, amount, currency, discounts, and plan permissions from server config or Stripe. Accept an allowed product choice from the browser, not a trusted price or customer ID.
3. Allow only known return URLs. Use an idempotency key for retried session, refund, or other money-changing requests.
4. Show a pending state after return. Grant access from verified billing state, not a success URL.

## 3. Handle webhooks safely
Verify Stripe's signature against the raw request body and the right environment's signing secret before processing. Reject invalid signatures.

Store each event ID under a unique constraint. Apply the billing update and mark the event complete atomically, or use a retry-safe state machine. A crash after receipt must allow retry. Return success for completed duplicates. Return a retryable failure if processing fails.

Handle delayed and out-of-order events. Fetch current Stripe state when needed. Sync subscription status, customer, subscription ID, period end, and cancellation state to a table with RLS. Let users read only their own billing summary; let only trusted backend code change entitlements. Enforce access on the server too.

## 4. Finish and prove the flow
Provide refund and cancel paths. Check the caller's rights, explain timing and access changes, and sync the result from Stripe. Cover failed payments, renewal, expiry, and pending cancellations.

Use Stripe test mode to check checkout success, declined payment, abandoned checkout, duplicate and out-of-order events, invalid signatures, interrupted processing and retry, refund, and cancellation. Confirm both the table and app access after each case. Run `rls-leak-check` for access tests. Report test-mode evidence and any live setup left unchecked. Ask for approval before enabling live billing.
