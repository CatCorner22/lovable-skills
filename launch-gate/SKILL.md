---
name: launch-gate
description: Use when the user is about to publish, launch, go live, connect a custom domain, or share the app with real users. Runs one go or no-go review across security, payments, login, user experience, search, and operations.
---

# Launch gate

Give 1 clear answer: go or no-go, with the reasons.

## Checks
| Area | Check |
|---|---|
| Security | Run the deep security scan (it never runs by itself) and fix critical and high findings. Run `rls-leak-check`. No secret keys in client code. |
| Abuse | For apps with logins, payments, or personal data, run `red-team-review` or confirm it passed after the last big change. |
| Login | Sign up, sign in, sign out, password reset, and email confirmation all work. Signed-out users cannot reach private pages. |
| Payments | Webhooks verify their signature on the server. A repeated webhook does not charge or grant twice. Prices come from the server, not the browser. Test mode is off only when ready. |
| User experience | Every page has loading, empty, and error states. Works on phone, tablet, and desktop. Run the built-in accessibility check. |
| Copy | Plain words, short sentences, active voice. No placeholder text or lorem ipsum. |
| Search | Run the built-in SEO and AI search review. Titles, descriptions, and social preview images are set. |
| Legal | Privacy policy and terms exist if the app collects personal data or takes payments. |
| Operations | Custom domain and HTTPS work. Backups or version history are known. Usage limits and alerts are set. |

## Output
A table: area, result (pass, fail, n/a), and the fix for each fail. Then 1 line: GO, or NO-GO with the blocking items.
