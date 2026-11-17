# Query and scale checks

Work in this order: query performance, connection use, access rules, schema, locking, data access, diagnostics, then advanced features. Optimize a measured path rather than a guess.

## Query performance
Capture query shape, table size, latency, and environment. Use EXPLAIN first. Use EXPLAIN ANALYZE only where executing the statement is safe; it runs the query. Compare actual rows with estimates. Check sequential scans, repeated loops, sort spills, and rows removed by filters.

Index common filters and joins. Put equality columns before range columns in a composite index when that matches the query. Use partial indexes for a stable filtered subset and covering indexes only when read gains justify write and storage cost. Verify that the plan uses the index at realistic sizes. Refresh statistics when stale estimates matter.

Example: a tenant's latest invoices often need an index on `(tenant_id, created_at, id)` and a matching stable order. Check the actual workload before adding it.

## Connections and access
Reuse clients where the runtime allows it. Use the supported pooler for the deployment model. Bound concurrency and transactions. Check pool limits, timeouts, and prepared-statement compatibility against current docs. Keep slow network calls outside transactions.

Review policy predicates and supporting indexes. Avoid per-row repeated work where a safe equivalent exists. Preserve access semantics while tuning. Use rls-leak-check for isolation tests.

## Schema and locks
Choose types for the real range of values. Normalize shared facts; denormalize only with a clear update owner. Bound JSON fields and index only queried paths. Measure each added index's write cost.

Use short transactions and a consistent lock order. Prefer atomic updates to read-then-write races. Handle unique conflicts and retryable failures explicitly. Plan large index builds and backfills around live traffic and lock behavior.

## Data access and diagnostics
Select needed columns. Batch N+1 reads and writes. Use keyset pagination for large changing lists where appropriate; make the sort unique. Bound exports and API responses. Cache only with a clear freshness and invalidation rule.

Use slow-query logs and query statistics when available. Compare before and after under similar data and load. Record row counts, latency, plans, and tradeoffs. Consider partitioning, full-text search, or vector indexes only for a measured need and verified platform support.
