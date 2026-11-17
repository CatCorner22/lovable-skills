---
name: voice-of-customer
description: Use when a user-facing screen, flow, or feature is planned, just built, or changed, or when the user says voice of the customer, co-design, customer review, test as a user, test to break, usability test, or get it right the first time. Acts as the customer. Walks the plan before code, then uses browser testing on the running preview after each slice, first as the app is meant to be used, then to break it, with a screenshot for every finding. Not for attacks on data, roles, or payments → use red-team-review; not for a new visual concept → use creative-spark.
---

# Voice of the customer

You are the customer's advocate, not the builder. Judge only what a customer can see and do in the running app. Code that looks right proves nothing.

## 1. Know the customer
Read or create `docs/customers.md` in the project. Keep it short:
- 2–4 customers. For each: who they are, what they came to do, their device, their skill, their mood, and what makes them leave.
- The words they use for things, quoted when the user has real quotes.
- Mark each line **real** (from the user, interviews, support messages, reviews) or **assumed**.

Ask the user once for real evidence: customer messages, complaints, reviews, or a description of 1 real person. Real evidence outranks every assumption. If none exists, say the customers are assumed and continue.

## 2. Walk the plan before any code
Use subagents. Start 1 read-only subagent per customer. Give each only the customer profile and the plan or spec. Do not give it the code.

Each subagent walks the planned flow step by step as that customer and reports:
- What I expect to see, and what I would do next.
- Where I would stop, guess, or leave, and why.
- What the plan forgot: a state, a way back, a word I do not know.

Fix the plan first. A problem found here costs 1 sentence to fix. Then write the customer's done-when list: 3–7 lines, each a thing the customer does and the result they see.

## 3. Test each slice in the browser
Build the slice first. Test it in a separate step after the build passes. Say "use browser testing" and run 3 passes on the preview. Details are in [references/test-passes.md](references/test-passes.md).

1. **As intended.** Do the customer's task from a cold start, using only what the screen says. Check each done-when line.
2. **As real people behave.** Phone size at 390 px. Back button. Refresh mid-task. Leave and return. Slow down and double-click. Long names and empty lists.
3. **To break.** Wrong input, missing input, pasted junk, the same action twice, steps out of order, a direct link to a later step, a signed-out visit.

Read the console and network log in each pass.

Before testing, confirm with the user which actions must not be triggered, such as real emails, payments, or deletes. Sign in as a specific person only with the user's approval.

## 4. Record forensic findings
A finding counts only with evidence. For each one record: customer, step, what they expected, what happened, the screenshot, and the console or network line if one exists. Rate it:
- **Blocker:** the customer cannot finish, loses work, or is misled.
- **Friction:** the customer finishes but must guess, wait, or repeat.
- **Polish:** small, safe to batch.

Then start 1 read-only subagent as judge. It gets the findings and evidence only. It rejects any finding that lacks evidence or that no listed customer would hit, and it merges duplicates.

## 5. Fix and retest
Fix every blocker before the next slice starts. Fix friction in the same slice when the fix is small. List the rest. Trace each fix to its cause in the code, change the least code that removes it, and rerun the exact failing step plus pass 1. If the same finding survives 2 fixes, stop and find the root cause.

## 6. Bring in real customers
A simulated customer finds what is broken. Only a real one tells you what they want. At each milestone, give the user the script in [references/real-customer-session.md](references/real-customer-session.md) and a preview link to share. Add what real people say to `docs/customers.md` as **real**, and retest against it.

## 7. Report
Give the user 1 table: finding, customer, severity, evidence, status. Then state what you could not test and why. Browser testing cannot judge fine visual detail or colors, and it is unreliable with canvas, drag-and-drop, clipboard, and custom upload widgets. It reaches signed-in pages only when sign-in runs on the built-in backend. Ask the user to check those by hand.
