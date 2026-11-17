# Lean-code rules (lens D)

Apply these to every line. Project conventions win if they conflict.

## Structure
- One job per function and per component. Split anything over ~50 lines.
- Reuse existing helpers, components, and hooks before you write new ones.
- Keep data access in one layer. Components do not build raw queries.
- No new dependency when the platform or an existing one already does the job.

## Types and data
- Strict TypeScript. No `any`. Type every function input and output.
- Validate all outside input (forms, URL params, API bodies) at the edge, for example with zod.
- Never trust the browser. Check permissions on the server or in row-level security.
- Fetch only the columns you use. Page long lists. No query inside a loop.

## Control flow
- Return early. Avoid nesting deeper than 3 levels.
- Handle loading, empty, and error states for every data view.
- Await every promise. Catch errors where you can act on them, and show the user a clear message.

## Naming and size
- Names say what a thing is or does. No `data2`, `temp`, or `handleStuff`.
- Constants for magic numbers and strings.
- Comments only to explain why, never what.

## Leave it clean
- No dead code, commented-out code, unused imports, or `console.log` left behind.
- No secret keys in client code. Secrets live in backend secrets only.
- Each slice ends with a passing build and no new warnings.
