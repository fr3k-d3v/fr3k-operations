#!/usr/bin/env python3
import subprocess,json,pathlib,datetime
names=['frappe/hrms','frappe/erpnext','horilla/horilla-hr','makeplane/plane','opf/openproject','kimai/kimai','calcom/cal.com','temporalio/temporal','n8n-io/n8n','odoo/odoo','crewAIInc/crewAI','logan-han/taxman','8bu/crewdoku','jaxjixmix/openRoster','crewcircle/crewRoster']
rows=[]
for n in names:
 try:
  r=json.loads(subprocess.check_output(['gh','api','repos/'+n],stderr=subprocess.DEVNULL,timeout=15))
  row={'repo':n,'status':'FOUND','stars':r['stargazers_count'],'license_api':(r.get('license') or {}).get('spdx_id'),'updated':r.get('pushed_at'),'archived':r['archived'],'default_branch':r['default_branch'],'open_issues':r['open_issues_count'],'url':r['html_url']}
 except Exception as e:row={'repo':n,'status':'UNVERIFIED_OR_MISSING','error':str(e)[:100]}
 rows.append(row);print(n,row['status'],row.get('license_api'),flush=True)
pathlib.Path('research/shortlist-audit.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'metadata only; licence compatibility, security and test quality not verified','repos':rows},indent=2))
s=['# Shortlist metadata audit','This is a **read-only GitHub API check**, not source/security validation. No third-party code imported.','','| Repo | Status | Stars | API licence | Last push |','|---|---|---:|---|---|']
for r in rows:s.append(f"| {r['repo']} | {r['status']} | {r.get('stars','—')} | {r.get('license_api','UNKNOWN')} | {r.get('updated','—')} |")
s+=['','## Integration decision gates','1. Review full licence, notices and copyleft obligations; API SPDX metadata is insufficient.','2. Pin source SHA and inspect dependencies, security advisories, auth, migration/backup and tests.','3. Build isolated synthetic-data POC; no real HR data.','4. Evaluate against FR3K immutable-history requirements and Australian compliance boundaries.','5. Adopt by adapter or module only after review; do not vendor source blindly.']
pathlib.Path('research/shortlist-audit.md').write_text('\n'.join(s)+'\n')
