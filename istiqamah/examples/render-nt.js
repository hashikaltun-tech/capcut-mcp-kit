const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const j of JSON.parse(fs.readFileSync('build/nt.json'))){await p.goto('file://'+path.resolve(j));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
 const m=await p.evaluate(()=>{const r=e=>e.getBoundingClientRect();let maxB=0,maxR=0,minL=1e4;
  document.querySelectorAll('.content *').forEach(e=>{const q=r(e);if(q.width&&q.height){maxB=Math.max(maxB,q.bottom);maxR=Math.max(maxR,q.right);minL=Math.min(minL,q.left)}});
  const t=document.querySelector('.tease');const v=document.querySelector('.vis');
  return {bottom:Math.round(maxB),right:Math.round(maxR),left:Math.round(minL),teaseTop:t?Math.round(r(t).top):null,visOverflow:v?v.scrollHeight-v.clientHeight:0,fonts:[...document.fonts].filter(f=>f.status=='loaded').length}});
 console.log(j,JSON.stringify(m));await p.screenshot({path:j.replace('.html','.png'),omitBackground:true});}
await b.close();})();
