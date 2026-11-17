---
name: credit-saver
description: Use when the user mentions credits, cost, or running out, or asks to batch, plan, or save usage. Sends each request to the cheapest mode that can do it and groups small edits into one message.
---

# Credit saver

Spend credits on changes, not on talk or rework.

## Pick the cheapest mode that works
| Need | Mode | Why |
|---|---|---|
| A question, an idea, or a choice between options | Chat mode | Costs a fraction of a credit. Never changes code. |
| A larger or risky change that needs a design | Plan mode | About 1 credit per message plus research. Approve the plan before building. |
| A clear, approved change | Build mode | Do it in 1 message with full detail. |
| A big task that must finish completely | Goal (`/goal`) | Only when a complete result matters more than cost. It can run for hours. |

## Write messages that land the first time
- Say what, where, and how it should look and behave. Name the page and the component.
- Group related small edits (copy, colors, spacing) into 1 message.
- Use the visual editor for text and style tweaks instead of a chat message.
- Attach a screenshot for layout problems.

## Avoid paying twice
- After 2 failed fixes, stop and use `error-loop-breaker` instead of retrying.
- Revert to a working version instead of stacking fixes on broken code.
- Try experiments in a draft, so a failed idea does not need a cleanup message.

## Check usage
Before a large task, say roughly how big it is and which mode you will use. Suggest a usage limit or alert in workspace settings if spend is a concern.
