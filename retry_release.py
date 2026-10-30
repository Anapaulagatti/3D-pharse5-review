"""One bounded rerun of a failed, already owner-approved exact release.
Does not approve environments, change payloads or modify protection rules.
"""
from pathlib import Path
import json,urllib.request,os
repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN'];r=json.loads(Path('release-retry/request.json').read_text());q=json.loads(Path('approved-releases/current.approved.json').read_text())
assert repo=='Anapaulagatti/3D-pharse5-review'
assert q['decision']=='APPROVED_PUBLIC_PREVIEW'and q['artifactCommit']==r['artifactCommit']and q['manifestSHA256']==r['manifestSHA256']
def call(path,data=None):
 req=urllib.request.Request('https://api.github.com/repos/'+repo+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Cache-Control':'no-cache'},data=None if data is None else json.dumps(data).encode(),method='GET'if data is None else'POST')
 with urllib.request.urlopen(req,timeout=30)as response:
  raw=response.read();return response.status,json.loads(raw)if raw else None
cleanup=Path('release-retry/cleanup.json')
if cleanup.exists():
 c=json.loads(cleanup.read_text());assert c['runId']==r['runId']and c['artifactId']==12984622473
 _,run=call('/actions/runs/'+str(r['runId']));assert run['head_sha']==r['controlCommit']and run['run_attempt']==2 and run['status']in ['waiting','in_progress','queued']
 _,artifact=call('/actions/artifacts/'+str(c['artifactId']));assert artifact['name']=='github-pages'and artifact['workflow_run']['id']==r['runId']
 req=urllib.request.Request('https://api.github.com/repos/'+repo+'/actions/artifacts/'+str(c['artifactId']),headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'},method='DELETE')
 with urllib.request.urlopen(req,timeout=30)as response:assert response.status==204
 print('Removed only stale failed attempt1 transport upload12984622473 to prevent immutable-name conflict on retry. Canonical artifact74235a6e, all Git checkpoints and old20 snapshot unchanged; no environment approval performed.')
 raise SystemExit(0)
_,run=call('/actions/runs/'+str(r['runId']));assert run['head_sha']==r['controlCommit'];assert run['status']=='completed'and run['conclusion']=='failure';assert run['run_attempt']==1,'Only a single retry is authorized by this controlled request'
_,history=call('/actions/runs/'+str(r['runId'])+'/approvals');assert any(v['state']=='approved'and v['user']['login']=='Anapaulagatti'and any(e['name']=='github-pages'for e in v['environments'])for v in history),'Original environment review must have been legitimately approved'
status,_=call('/actions/runs/'+str(r['runId'])+'/rerun-failed-jobs',{});assert status==201
print('Requested one rerun of failed jobs for exact owner-approved release',r['runId'],'HTTP',status,'; environment protections remain enforced by GitHub')
