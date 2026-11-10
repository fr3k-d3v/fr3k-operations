#!/usr/bin/env python3
"""Read-only GitHub candidate inventory. Public metadata only."""
import json, subprocess, datetime, pathlib, time
queries=[
 'topic:hrms stars:0','topic:workforce-management stars:0',
 'topic:rostering stars:0','topic:payroll stars:0',
 'topic:project-management stars:0',
 'topic:workforce-management stars:1..5',
 'topic:hrms stars:1..5',
 'topic:time-tracking stars:1..5',
 'topic:hrms stars:>50',
 'topic:workforce-management stars:>50',
 'topic:project-management stars:>100',
 'topic:workflow-engine stars:>50',
 'australian payroll in:name,description',
 'xero integration in:name,description',
 'award interpretation in:name,description'
]
results={}
for q in queries:
 try:
  raw=subprocess.check_output(['gh','api','search/repositories','-f','q='+q,'-f','per_page=30','--method','GET'],stderr=subprocess.DEVNULL,timeout=25)
  obj=json.loads(raw)
  for x in obj.get('items',[]):
   n=x['full_name']; z=results.setdefault(n,{'name':n,'url':x['html_url'],'description':x.get('description'),'stars':x['stargazers_count'],'updated':x['updated_at'],'license':(x.get('license') or {}).get('spdx_id'),'archived':x.get('archived',False),'topics':x.get('topics',[]),'queries':[]})
   z['queries'].append(q)
  print(q,len(obj.get('items',[])),flush=True)
 except Exception as e: print('ERROR',q,str(e)[:90],flush=True)
 time.sleep(.3)
out=sorted(results.values(),key=lambda r:(-len(r['queries']),-r['stars']))
pathlib.Path('research/github-inventory.json').write_text(json.dumps({'collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'GitHub search API metadata; no code audited','queries':queries,'repos':out},indent=2))
lines=['# GitHub candidate inventory','Generated from live public GitHub search metadata. Discovery is not endorsement or licence approval.','',f'Unique repos: **{len(out)}**. Search includes zero-star and 1–5-star candidates.','', '| Repository | Stars | Licence (API) | Matched searches |','|---|---:|---|---:|']
for r in out[:100]:lines.append(f"| [{r['name']}]({r['url']}) | {r['stars']} | {r['license'] or 'UNKNOWN'} | {len(r['queries'])} |")
pathlib.Path('research/github-inventory.md').write_text('\n'.join(lines)+'\n')
