---
name: ux-engineering
description: Use when improving task flows, forms, onboarding steps, recovery, or loading, empty, error, and success states. Focuses on usable behavior. Not for visual style and tokens → use evidence-based-ui-design; use Lovable's built-in accessibility skill for a dedicated accessibility audit.
---

# UX engineering

Help the user finish the task with clear feedback and recoverable errors.

## 1. State the outcome
Name the actor, skill level, stress context, job, success signal, and likely failures. For a new feature with missing goals, use `feature-spec`.

For flows with 2 or more steps, sketch entry → steps → success, with back, cancel, and recovery branches. Keep deep links where the app supports them.

## 2. Cover every state
| State | Pattern |
|---|---|
| Loading | Show work in progress; use a skeleton that matches the layout. |
| Empty | Explain why nothing appears and offer the first action. |
| Error | State what happened, preserve input, and offer retry or a support path. |
| Success | Confirm the result and next step instead of a silent redirect. |

## 3. Review the 10 heuristics
Check system status; real-world words; user control and undo; consistent labels and placement; error prevention; visible choices instead of memory tests; shortcuts that preserve a simple novice path; minimal noise; clear error recovery; and help at the point of need.

For forms, use real labels rather than placeholders alone. Validate after blur or submit unless a useful live check needs input. Explain why submit is unavailable. Show errors near their fields and preserve entered data on server failure. Explain destructive effects before confirmation.

Use specific verbs: “Save changes”, not “Submit”. “No invoices yet — create your first invoice” gives an empty state a job. Use `plain-copy` for a full copy pass.

## 4. Check access and feedback
Keep every critical flow keyboard-operable with a logical tab order and visible focus. Use text or icons with status colors. Check normal-text contrast at 4.5:1. Give inputs labels and buttons useful names. Announce async results with an appropriate live region. Honor reduced-motion settings. Use the built-in accessibility skill for deeper coverage.

## 5. Verify behavior
Test normal, empty, loading, and failed states. Enter invalid values, retry after failure, use back and cancel, and confirm that saved state survives refresh. Test the main flow with a keyboard. Use actual rendered evidence for visual claims.

Return flow changes, checked states, results, and untested cases. A good-looking still image alone does not prove a usable flow.
