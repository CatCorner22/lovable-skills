---
name: evidence-based-ui-design
description: Use when choosing a visual direction, design tokens, or a distinctive screen style for a Lovable app. Grounds layout choices in the user's task and checks the rendered result. Not for task-flow repair → use ux-engineering; use Lovable's built-in accessibility skill for a dedicated accessibility audit.
---

# Evidence-based UI design

Make design choices explicit. Keep familiar navigation. Spend boldness in 1 place.

## 1. Write the product contract
State the user and their skill or stress level; the job the screen answers in 5 seconds; 1 primary action; real content; loading, empty, error, success, and long-text states; and the category norms users expect. Label assumptions. Use honest example data in a draft; mark it as example data.

## 2. Set tokens and direction
Use 4–6 core colors: ink, paper, line, muted, and 1 accent, plus status colors with clear meaning. Use at most 2 type roles, tabular digits for numbers, a 4 or 8 px spacing scale, 1 radius, and 1 shadow or none. Define CSS variables first.

Name a real visual reference and why it fits the subject. If the user has no preference, offer 3 distinct directions, then build the chosen one. Reuse the app's existing design system where it works.

## 3. Apply the design checks
- Put the answer and main action in the first viewport, along the expected reading path.
- Show 1 primary action. Recommend a default. Start with at most 4 key options or numbers; group the rest.
- Group with space and alignment before adding boxes.
- Give color a purpose. Pair status color with text or an icon.
- Start body text at 16 px, lines near 65 characters, and line height 1.4–1.6. Favor light backgrounds for long reading unless context calls for another choice.
- Check contrast: 4.5:1 for normal text; 3:1 for large text and UI parts. Keep focus visible. Use targets at least 24×24 CSS px; aim for 44 px on touch. Offer an alternative to dragging.
- Give instant local feedback where possible. Past 1 second, show loading; past 10 seconds, show progress and cancel when safe.
- Keep motion purposeful and honor reduced-motion settings.
- End flows with a clear result and next step.

Treat perception and timing rules as design heuristics, not universal scientific guarantees.

## 4. Keep the design honest
Make cancel and change easy. Show real costs and real progress. Use user words and specific verbs. Favor subject-led type and imagery over default gradients, glow buttons, blurred orbs, nested cards, vanity stats, sparkle badges, and vague “AI-powered” claims. Refresh the cliché list as styles change.

## 5. Render and critique
Build semantic HTML with labels and useful alt text. Inspect the actual preview at 1440 and 390 px when available. Check the contract, hierarchy, keyboard focus, contrast, targets, and every state. Remove 1 needless decoration. Fix the top 3 issues and inspect again. Show before/after evidence when available. State any viewport or interaction you could not check.
