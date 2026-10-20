// Greenhouse (job-boards.greenhouse.io) background-safe fill helpers. Works when Chrome is minimized/hidden.
// Field-tested on dozens of live Greenhouse forms (Oct 2026). Generalized: set GH.FILES to a regex that
// matches the uploaded file names (default: any .pdf), and pass the candidate's city to GH.loc / run().
// ORDER MATTERS (form state updates use the last rendered snapshot, so later writes can wipe earlier ones):
//   1) file_upload resume/cover letter (Claude in Chrome file_upload tool). Later state writes can wipe an upload: run() refuses to submit unless minFiles PDFs are attached; if one vanished, re-upload it and submit after re-checking
//   2) paste this file, then:  await GH.fix(SPEC)  where SPEC=[[id,query,label],...] (sets, re-checks, re-sets until values stick; question_* selects can't be read back, they are set once)
//   3) await GH.txtAll([[id,value],...])                                  (text/textarea via React onChange)
//   4) await GH.loc('<City>','<City, State, United States>')            (LAST; only if form has candidate-location)
//   5) GH.check() -> verify, then GH.submit(); wait ~15s; confirm URL ends with /confirmation, else GH.errors()
// Easiest: await GH.run(SPEC, TEXTS, CHECKBOX_IDS, ['Houston','Houston, Texas, United States'] or null, doSubmit)  (question_* dropdowns first in SPEC)
window.tick=()=>new Promise(r=>{const c=new MessageChannel();c.port1.onmessage=()=>r();c.port2.postMessage(0)});
window.ticks=async n=>{for(let i=0;i<n;i++) await tick()};
window.GH = {
  FILES: /[\w.-]+\.pdf/g,
  fiber(id){const e=document.getElementById(id); if(!e) return null; const k=Object.keys(e).find(k=>k.startsWith('__reactFiber')); return e[k];},
  find(id,test){let f=GH.fiber(id); for(let i=0;i<50&&f;i++,f=f.return){const p=f.memoizedProps; if(p&&typeof p==='object'&&test(p)) return p;} return null;},
  rs(id){return GH.find(id,p=>p.inputId===id&&typeof p.onChange==='function'&&('options' in p||p.loadOptions));},
  app(id){return GH.find(id,p=>typeof p.onSelect==='function'&&'selected' in p);},
  val(id){const a=GH.app(id), r=GH.rs(id); const v=(a&&a.selected)||(r&&r.value); return v?(Array.isArray(v)?v.map(x=>x.label).join(','):v.label):'';},
  async opts(id,q){const p=GH.rs(id)||{}; let o=p.options||[]; const a=GH.app(id); const load=p.loadOptions||(a&&a.loadOptions);
    if(load){const r=await load(q||'',[],{page:1}); o=(r&&r.options)||r||[];} return o.flatMap(x=>x.options?x.options:[x]);},
  async sel(id,q,label){const all=await GH.opts(id,q); const re=label instanceof RegExp?label:null;
    const o=all.find(x=>re?re.test((x.label||'').trim()):(x.label||'').trim()===label);
    if(!o) return 'NF '+id+': '+all.slice(0,25).map(x=>x.label).join(' / ');
    const a=GH.app(id); if(a) a.onSelect(o); else { const r=GH.rs(id); r.onChange(o,{action:'select-option',option:o}); }
    await ticks(60); return 'ok '+id+'='+o.label;},
  fval(id){const p=GH.find(id,p=>'uploadManager' in p&&'value' in p); return p?p.value:undefined;},
  ok(id,l){if(/^question_/.test(id)){const v=GH.fval(id); return v!==undefined&&v!==null&&v!=='';} const v=GH.val(id); return l instanceof RegExp?l.test(v):v===l;},
  async fix(list,passes=5){let log=[]; for(let p=0;p<passes;p++){const bad=list.filter(([id,q,l])=>!GH.ok(id,l)); if(!bad.length){log.push('pass'+p+':ok');break;} log.push('pass'+p+':'+bad.map(b=>b[0].slice(-8)).join(',')); for(const b of bad){await GH.sel(...b); for(let i=0;i<400&&!GH.ok(b[0],b[2]);i++) await tick();}} return log.join(' | ');},
  async checks(ids){for(const id of ids){const e=document.getElementById(id); if(e&&!e.checked){e.click(); await ticks(40);}} return ids.map(id=>document.getElementById(id).checked).join(',');},
  // One call: dropdowns -> checkboxes -> texts -> location -> verify -> submit (only if everything verified). Use on a FRESH page load (a failed submit leaves sticky errors; reload and rerun).
  async run(spec,texts,checks,loc,doSubmit,minFiles=1){const out=[]; out.push(await GH.fix(spec)); if(checks&&checks.length) out.push('checks:'+await GH.checks(checks));
    out.push(await GH.txtAll(texts)); out.push(await GH.fix(spec,3));
    for(const [id,v] of texts){ if(/^question_/.test(id)){ for(let k=0;k<3&&String(GH.fval(id)||'').length<Math.min(5,v.length);k++){ await GH.txt(id,v); for(let i=0;i<200&&!GH.fval(id);i++) await tick(); } } }
    if(loc){let r=await GH.loc(loc[0],loc[1]); if(/no options/.test(r)) r=await GH.loc(loc[0],loc[1]); out.push(r);}
    const bad=spec.filter(([id,q,l])=>!GH.ok(id,l)).map(s=>s[0]); const tbad=texts.filter(([id,v])=>{const fv=GH.fval(id); const e=document.getElementById(id); return /^question_/.test(id)?String(fv||'').length<Math.min(5,v.length):e.value.length===0;}).map(t=>t[0]);
    const locOk=!loc||!!(GH.find('candidate-location',p=>'uploadManager' in p&&'location' in p)||{}).location;
    out.push('bad:'+bad.join(',')+' tbad:'+tbad.join(',')+' locOk:'+locOk+' files:'+(document.body.innerText.match(GH.FILES)||[]));
    const nf=(document.body.innerText.match(GH.FILES)||[]).length;
    if(doSubmit&&!bad.length&&!tbad.length&&locOk&&nf>=minFiles){GH.submit(); await ticks(30); out.push('SUBMITTED-CLICK');}
    return out.join(' || ');},
  async selAll(list){const out=[]; for(const [id,q,l] of list) out.push(await GH.sel(id,q,l)); return out.join(' | ');},
  async txt(id,v){const e=document.getElementById(id); if(!e) return 'missing '+id; const P=e.tagName==='TEXTAREA'?HTMLTextAreaElement:HTMLInputElement;
    Object.getOwnPropertyDescriptor(P.prototype,'value').set.call(e,v); const k=Object.keys(e).find(k=>k.startsWith('__reactProps'));
    if(e[k]&&e[k].onChange) e[k].onChange({target:e,currentTarget:e}); else e.dispatchEvent(new Event('input',{bubbles:true}));
    await ticks(40); return id+':'+e.value.length;},
  async txtAll(list){const out=[]; for(const [id,v] of list) out.push(await GH.txt(id,v)); return out.join(' ');},
  async loc(q,label){ // needs real provider objects: temporarily run timers immediately so the debounced search fires in a hidden tab
    const orig=window.setTimeout; let n=900000; window.__cancel={};
    window.setTimeout=function(fn,d,...a){if(typeof fn!=='function') return orig(fn,d,...a); const id=++n; const ch=new MessageChannel(); ch.port1.onmessage=()=>{if(!window.__cancel[id]) fn(...a)}; ch.port2.postMessage(0); return id};
    const F=()=>GH.find('candidate-location',p=>typeof p.onSelect==='function'&&typeof p.onInputChange==='function');
    try{ F().onInputChange(q.slice(0,-1),{action:'input-change'}); await ticks(5); F().onInputChange(q,{action:'input-change'});
      let opts=null; for(let i=0;i<4000;i++){await tick(); const b=F(); if(b.options&&b.options.length){opts=b.options;break;}}
      if(!opts) return 'loc: no options (call again)';
      const o=opts.find(x=>x.label===label)||opts[0]; await F().onSelect(o); await ticks(60);
      const p=GH.find('candidate-location',p=>'uploadManager' in p&&'location' in p); return 'loc='+(p&&p.location);
    } finally { window.setTimeout=orig; } },
  fields(){return [...document.querySelectorAll('input,textarea')].filter(e=>e.type!=='hidden'&&e.id&&!e.id.startsWith('iti')&&!e.id.startsWith('g-recaptcha')).map(e=>e.id+'|'+e.type+'|'+((document.querySelector('label[for="'+e.id+'"]')||{}).innerText||'').replace(/\s+/g,' ').slice(0,80));},
  check(){return [...document.querySelectorAll('input,textarea')].filter(e=>e.id&&!e.id.startsWith('iti')&&!e.id.startsWith('g-recaptcha')&&e.type!=='hidden'&&e.type!=='file').map(e=>{const s=GH.val(e.id); return e.id+'='+(s||(e.type==='checkbox'?e.checked:e.value.slice(0,25)));}).join(' | ')+' | files:'+(document.body.innerText.match(GH.FILES)||[]);},
  errors(){return [...document.querySelectorAll('[class*=error],[role=alert]')].map(e=>e.innerText).filter(Boolean);},
  submit(){document.querySelector('button[type=submit]').click(); return 'clicked';}
};
'GH ready';
