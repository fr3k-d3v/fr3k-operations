# Connected CREW CENTRAL web workspace

Updated: 2026-11-11. Private application increment: `ec94886`.

The Django application now opens on a connected operations overview at `/`.
It uses the existing database, memberships and versioned records.

- Live review counts, approved shifts for today, outstanding assignments and
  upcoming company/document dates.
- Company selection and role-specific module navigation for people/recruitment,
  workforce/time, projects/finance and documents/company.
- Direct links to the real forms, time clock, leave balances, costing, registers,
  documents and review queues.
- Searchable module record pages with company/type filters and review badges.
- Owner/admin settings and read-only owner/admin/auditor access review in web
  pages, using the same authorization and audit services as the API.
- Responsive mobile navigation, a worker time-clock shortcut and refreshed
  sign-in screens.

No totals are fabricated. Workers do not receive HR/pay-source records, other
company records are excluded, and drafts do not replace approved roster versions.

## Verification

Local PostgreSQL verification passed 203 Django tests without skips, four
standalone checks and five Chromium journeys, plus migration/OpenAPI,
dependency and static checks. The added browser journey signs in, navigates to
projects, searches live records, creates a job through its form, sees it on the
overview, saves owner settings, inspects access review, and tests worker mobile
navigation/time-clock access. Keyboard skip navigation, page errors and mobile
overflow were checked.

The screenshots and application source are retained privately. Hosted CI for
this increment is recorded on the [current progress page](CREW-CENTRAL-IMPLEMENTATION.md).

## Use and release boundary

The local application starts with `make demo`; enable an individual synthetic
account with the documented password command and open http://127.0.0.1:8000.
Existing query URLs such as `/?view=roster` remain supported, while
`/workspace/` is the full record browser.

This is an implemented web interface, not a claim of a public hosted deployment.
Production stays disabled pending the previously recorded identity, recovery and
other acceptance gates. The owner's deferred decisions remain pending.
