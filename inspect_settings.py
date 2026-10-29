"""Read-only GitHub configuration inspection; emits selected nonsecret fields only."""
import urllib.request,urllib.error,json,os,datetime
repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN'];out={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':repo,'runId':os.environ['GITHUB_RUN_ID'],'publicationAttempted':False,'checks':{}}
def get(name,path,select):
 request=urllib.request.Request('https://api.github.com/repos/'+repo+path,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'})
 try:
  with urllib.request.urlopen(request,timeout=30)as r:out['checks'][name]={'status':r.status,'data':select(json.load(r))}
 except urllib.error.HTTPError as e:
  try:message=json.load(e).get('message')
  except Exception:message='Response not parsed'
  out['checks'][name]={'status':e.code,'message':message,'acceptedPermissions':e.headers.get('X-Accepted-GitHub-Permissions')}
 except Exception as e:out['checks'][name]={'error':str(e)}
get('pages','/pages',lambda q:{k:q.get(k)for k in ['status','html_url','build_type','source','https_enforced','public']})
get('actions','/actions/permissions',lambda q:{k:q.get(k)for k in ['enabled','allowed_actions']})
get('workflowPermissions','/actions/permissions/workflow',lambda q:{k:q.get(k)for k in ['default_workflow_permissions','can_approve_pull_request_reviews']})
get('deploymentWorkflow','/actions/workflows/review-pages.yml',lambda q:{k:q.get(k)for k in ['name','path','state']})
get('environment','/environments/github-pages',lambda q:{'name':q.get('name'),'protectionRules':[{'type':r.get('type'),'reviewerCount':len(r.get('reviewers',[])),'preventSelfReview':r.get('prevent_self_review')}for r in q.get('protection_rules',[])],'deploymentBranchPolicy':q.get('deployment_branch_policy')})
with open('settings-report.json','w')as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
