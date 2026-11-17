---
name: feature-spec
description: Use when the user asks for a new feature, page, or app and the request leaves open what it should do, who uses it, or what data it needs. Asks the questions first, then writes a short spec with done-when tests before any code.
---

# Feature spec

Fill the gaps before writing code. A clear spec saves more credits than any other step.

## Step 1. Ask first
Ask every open question in 1 message. Cover only what changes the build:
- Who uses it, and what are they trying to get done?
- What are the main steps, from start to finish?
- What data does it save, and who may see or change it?
- What happens when something goes wrong or a list is empty?
- Does it need login, payments, email, files, or AI?
- What is out of scope for now?

Where a guess is cheap to undo, make it and label it "Assumed".

## Step 2. Write the spec (1 screen long)
1. Goal: 1 sentence.
2. Users and roles.
3. Flow: numbered steps.
4. Data: tables, fields, owner, and who can read and write.
5. Screens: each page with its loading, empty, and error states.
6. Done when: 3 to 7 tests a user could run.
7. Out of scope.

## Step 3. Hand off
Get approval on the spec. Then build it with `four-lens-build`, one slice at a time. Keep the spec in project files so later changes can check against it.
