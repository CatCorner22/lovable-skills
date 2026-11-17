---
name: premise-check
description: Use when a request embeds a factual premise or diagnosis that could change the plan. Verifies it and tries to disprove it before acting. Not for repeated failed fixes → use error-loop-breaker; not for defining feature goals → use feature-spec.
---

# Premise check

Agreement is not evidence. Check the premise before you build on it.

## Steps
1. Extract each premise after “since”, “because”, or “given that”. Include claims about causes, versions, limits, and deprecated features.
2. Start with up to 3 small checks. Read the relevant code, reproduce the symptom, check the installed version, or open current docs. Use the actual app and backend environment.
3. Trace whether the suspect path runs in this user's case. Check the route, feature flag, role, and configuration.
4. Try to disprove the leading explanation. Check another caller, the opposite hypothesis, or a case where the cause is absent.
5. State the result first, then act:
   - Confirmed: premise, evidence, and the path that runs.
   - Premise does not hold: evidence and the changed plan.
   - Unverified: checks tried, missing evidence, and any labeled assumption.

Keep disagreement plain and brief. Separate an observed symptom from its proposed cause. Code that could cause a bug does not prove that it did.

If a check costs more than the task, state that limit. Proceed on a labeled assumption only when a wrong guess is cheap to undo. Ask before a guess changes user behavior or puts data at risk.

## Return
Give the premise, evidence, disconfirmation check, and next action. Use `claim-evidence-pairing` for confidence labels. Mark every untraced link as unverified.
