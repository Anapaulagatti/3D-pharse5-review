import fs from 'node:fs/promises';
let field;
async function grid(){if(field)return field;const m=JSON.parse(await fs.readFile(new URL('./qa-nav.json',import.meta.url)));const cells=new Uint8Array(m.w*m.h);m.rows.forEach((row,y)=>{for(let i=0;i<row.length;i+=2)cells.fill(1,y*m.w+row[i],y*m.w+row[i+1]);});field={...m,cells};return field;}
export async function createWalk(page,records){const f=await grid(),{w,h,cells}=f;
 return async function move(target,radius=10){const start=await page.evaluate(()=>[window.__GATE3__.x,window.__GATE3__.y]);const sx=Math.round((start[0]-2)/4),sy=Math.round((start[1]-2)/4);let chosen=-1,best=Infinity;
 for(let dy=-3;dy<=3;dy++)for(let dx=-3;dx<=3;dx++){const x=sx+dx,y=sy+dy,id=y*w+x;if(x<0||x>=w||y<0||y>=h||!cells[id])continue;const d=(x*4+2-start[0])**2+(y*4+2-start[1])**2;if(d<best){best=d;chosen=id;}}
 if(chosen<0)throw Error('No canonical walkable start '+JSON.stringify(start));
 const parent=new Int32Array(w*h);parent.fill(-1);const queue=new Int32Array(w*h);let head=0,tail=1,end=-1;queue[0]=chosen;parent[chosen]=chosen;
 while(head<tail){const u=queue[head++],x=u%w,y=Math.floor(u/w);if((x*4+2-target[0])**2+(y*4+2-target[1])**2<=radius**2){end=u;break;}for(const v of [x>0?u-1:-1,x+1<w?u+1:-1,y>0?u-w:-1,y+1<h?u+w:-1])if(v>=0&&cells[v]&&parent[v]<0){parent[v]=u;queue[tail++]=v;}}
 if(end<0)throw Error('No canonical route '+JSON.stringify(target));const ids=[end];while(ids.at(-1)!==chosen)ids.push(parent[ids.at(-1)]);ids.reverse();const points=[ids[0]];let dir=null;for(let i=1;i<ids.length;i++){const d=ids[i]-ids[i-1];if(dir!==null&&d!==dir)points.push(ids[i-1]);dir=d;}points.push(ids.at(-1));
 for(const id of points){const goal=[(id%w)*4+2,Math.floor(id/w)*4+2];let n=0,last=Infinity,stale=0;while(n++<240){const pos=await page.evaluate(()=>[window.__GATE3__.x,window.__GATE3__.y]);const dx=goal[0]-pos[0],dy=goal[1]-pos[1],d=Math.hypot(dx,dy);if(d<2.8)break;stale=Math.abs(last-d)<.05?stale+1:0;last=d;if(stale>15)throw Error('Actual movement blocked '+JSON.stringify({pos,goal}));const keys=[];if(Math.abs(dx)>1.5)keys.push(dx>0?'d':'a');if(Math.abs(dy)>1.5)keys.push(dy>0?'s':'w');for(const k of ['Shift',...keys])await page.keyboard.down(k);await page.waitForTimeout(Math.min(100,Math.max(18,d*7)));for(const k of [...keys,'Shift'])await page.keyboard.up(k);}if(n>=240)throw Error('Real movement timeout');}
 records.push({start,target,end:await page.evaluate(()=>[window.__GATE3__.x,window.__GATE3__.y]),length:(ids.length-1)*4,actualControls:true,collisionOverride:false});
 };}
