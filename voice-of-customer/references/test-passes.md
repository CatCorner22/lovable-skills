# Test passes

Run every pass in the preview with browser testing. Take a screenshot at each step that matters.

## Pass 1: as intended
- Start cold: signed out, no data, first visit.
- Find the way in from the first screen without help.
- Finish the main task. Count the steps and the fields.
- Check each done-when line.
- Confirm the result: the customer sees that it worked and what to do next.
- Come back later. The work is still there.

## Pass 2: as real people behave
- **Size:** 390 px phone, then tablet, then desktop. Nothing cut off, no sideways scroll, buttons reachable by thumb.
- **Navigation:** back button, forward button, refresh mid-task, open a step in a new tab.
- **Interruption:** leave mid-form and return. Is the work kept?
- **Pace:** double-click submit. Click while loading. Wait a long time, then act.
- **Content:** very long name, very short name, accents and emoji, 0 items, 1 item, 500 items.
- **Words:** does every label use the customer's word? Does every error say what happened and what to do?
- **Keyboard:** tab through the flow. Focus is visible. Enter submits.
- **States:** loading, empty, error, and success each show something useful.

## Pass 3: to break
- **Input:** empty, spaces only, too long, wrong type, negative number, past date, pasted text with line breaks, script-like text.
- **Order:** skip a step. Open a later step by its link. Repeat a finished step.
- **Repeat:** submit twice. Create the same thing twice. Delete, then act on the deleted thing.
- **Session:** act when signed out. Act after the session ends. Use 2 tabs with different states.
- **Failure:** what does the customer see when a request fails? Can they retry without losing work?
- **Limits:** hit every stated limit and go 1 past it.
- **Undo:** can the customer reverse each action that changes or removes their work?

## Reading the evidence
- A console error during a flow is a finding, even when the screen looks fine.
- A failed or repeated network request is a finding.
- A silent failure, where nothing happens after a click, is a blocker.
- A screenshot that shows the wrong state outranks code that looks right.

## When a step will not run
If browser testing fails on the same element twice, check for a hidden element, an icon-only button, or a broken state. Add a visible label or accessibility label if one is missing; that helps customers too. If it still fails, skip the element, record it as untested, and ask the user to check it by hand.
