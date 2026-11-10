# Shortlist metadata audit
This is a **read-only GitHub API check**, not source/security validation. No third-party code imported.

| Repo | Status | Stars | API licence | Last push |
|---|---|---:|---|---|
| frappe/hrms | FOUND | 9037 | GPL-3.0 | 2026-11-10T02:49:15Z |
| frappe/erpnext | FOUND | 41143 | GPL-3.0 | 2026-11-10T08:16:54Z |
| horilla/horilla-hr | FOUND | 1504 | LGPL-2.1 | 2026-11-10T09:40:14Z |
| makeplane/plane | FOUND | 62235 | AGPL-3.0 | 2026-11-10T09:07:24Z |
| opf/openproject | FOUND | 17211 | GPL-3.0 | 2026-11-10T09:50:01Z |
| kimai/kimai | FOUND | 5148 | AGPL-3.0 | 2026-11-10T00:11:01Z |
| calcom/cal.com | FOUND | 49876 | MIT | 2026-11-03T21:35:09Z |
| temporalio/temporal | FOUND | 24299 | MIT | 2026-11-10T08:47:37Z |
| n8n-io/n8n | FOUND | 209985 | NOASSERTION | 2026-11-10T09:53:59Z |
| odoo/odoo | FOUND | 55681 | NOASSERTION | 2026-11-10T09:54:42Z |
| crewAIInc/crewAI | FOUND | 60720 | MIT | 2026-11-10T00:05:12Z |
| logan-han/taxman | FOUND | 0 | MIT | 2026-11-01T02:18:41Z |
| 8bu/crewdoku | FOUND | 0 | AGPL-3.0 | 2026-09-30T02:56:07Z |
| jaxjixmix/openRoster | FOUND | 0 | MIT | 2026-11-08T15:24:08Z |
| crewcircle/crewRoster | FOUND | 0 | NOASSERTION | 2026-11-06T08:12:52Z |

## Integration decision gates
1. Review full licence, notices and copyleft obligations; API SPDX metadata is insufficient.
2. Pin source SHA and inspect dependencies, security advisories, auth, migration/backup and tests.
3. Build isolated synthetic-data POC; no real HR data.
4. Evaluate against FR3K immutable-history requirements and Australian compliance boundaries.
5. Adopt by adapter or module only after review; do not vendor source blindly.
