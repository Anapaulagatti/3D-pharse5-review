"""Read one approved release run and its pending environment gate; never deploys/approves."""
from pathlib import Path
import urllib.request,urllib.error,json,os,datetime,time
repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN'];request=json.loads(Path('release-status/request.json').read_text());target=request.get('expectedControlCommit')or os.environ['GITHUB_SHA'];out={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inspectionRunId':os.environ['GITHUB_RUN_ID'],'expectedControlCommit':target,'publicationByThisJob':False,'checks':{}}
def get(path):
 req=urllib.request.Request('https://api.github.com/repos/'+repo+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 try:
  with urllib.request.urlopen(req,timeout=25)as r:return {'status':r.status,'data':json.load(r)}
 except urllib.error.HTTPError as e:
  try:message=json.load(e).get('message')
  except Exception:message='Unparsed HTTP response'
  return {'status':e.code,'message':message,'acceptedPermissions':e.headers.get('X-Accepted-GitHub-Permissions')}
 except Exception as e:return {'error':str(e)}
run=None
for attempt in range(5):
 q=get('/actions/workflows/review-pages.yml/runs?per_page=20');runs=q.get('data',{}).get('workflow_runs',[]);run=next((r for r in runs if r['head_sha']==target),None)
 if run:break
 if attempt<4:time.sleep(4)
if run:
 out['release']={k:run.get(k)for k in ['id','run_number','head_sha','status','conclusion','html_url','event','created_at','updated_at']};id=run['id'];q=get('/actions/runs/'+str(id)+'/jobs');out['jobs']={'status':q.get('status'),'items':[{k:j.get(k)for k in ['id','name','status','conclusion','html_url','started_at','completed_at']}for j in q.get('data',{}).get('jobs',[])]};q=get('/actions/runs/'+str(id)+'/pending_deployments');out['pendingDeployments']={'status':q.get('status'),'items':[{'environment':p.get('environment',{}).get('name'),'environmentId':p.get('environment',{}).get('id'),'currentUserCanApprove':p.get('current_user_can_approve'),'reviewers':[{'type':r.get('type'),'login':r.get('reviewer',{}).get('login'),'name':r.get('reviewer',{}).get('name')}for r in p.get('reviewers',[])]}for p in q.get('data',[]) ]if isinstance(q.get('data'),list)else[],'message':q.get('message'),'acceptedPermissions':q.get('acceptedPermissions')}
else:out['release']={'status':'NO MATCHING RELEASE RUN YET','lastReadStatus':q.get('status')}
Path('release-status.json').write_text(json.dumps(out,indent=2)+'\n')
