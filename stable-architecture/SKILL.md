---
name: stable-architecture
description: Use when splitting coupled modules, setting dependency boundaries, or making database and API adapters replaceable in a React/TypeScript app. Not for the full multi-file build process → use four-lens-build; not for database policy design → use supabase-best-practices.
---

# Stable architecture

Keep a testable core when the framework or backend changes.

## Dependency direction
Use the smallest useful form of:

`React UI / route / edge handler → application use-case → domain ← adapters`

Keep domain rules as plain TypeScript. Let adapters implement small interfaces that the core owns. Keep React, HTTP, and Supabase details at the edges.

| Part | Job |
|---|---|
| Domain | Entities, invariants, pure rules |
| Application | Use-cases, orchestration, transaction boundaries |
| Ports | Types for external needs |
| Adapters | Supabase queries, API clients, email delivery |
| Delivery | React screens, Vite or TanStack Start routes, edge handlers |

Skip parts that add no value. Split by feature and reason to change, not by folder count.

## Find weak seams
- Hidden shared state: pass data explicitly and narrow its scope.
- Circular imports: extract a port and move the implementation to an adapter.
- Large module with many jobs: split by use-case. A 500-line file is a review signal, not an automatic fault.
- Scattered flags: put capability decisions in 1 place.
- Tests that need the full app: use a fake adapter.
- Duplicated types: map external data once at the boundary.

Validate inputs, environment values, and API responses at system boundaries. Assert domain invariants with typed errors. Use TypeScript to rule out invalid states. Fail closed for money and authorization; keep silent security defaults out of the code.

## Build and check
Build vertical slices: screen → use-case → adapter, then the next feature. Favor a bounded monolith. Split services only for a demonstrated need for separate deployment, scaling, or failure isolation.

For a non-trivial feature, check:
1. Can a fake adapter test the use-case, including empty and failed responses?
2. Can another backend replace Supabase without changing domain rules?
3. Does the core still work without React or the route framework?

Add the missing seam before building more on a coupled base. Keep privileged operations on the server. Report changed boundaries, tests, and remaining coupling. Use `four-lens-build` for the wider build sequence.
