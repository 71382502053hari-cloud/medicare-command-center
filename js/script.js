/* MEDICARE shared interface behaviors */
const page = document.body.dataset.page || 'dashboard';
const navItems = [
  ['dashboard','index.html','⌂','Dashboard'],['infrastructure','infrastructure.html','▣','Infrastructure'],
  ['deployments','deployments.html','↑','Deployments'],['monitoring','monitoring.html','▥','Monitoring'],
  ['security','security.html','◇','Security'],['logs','logs.html','≡','Activity Logs'],
  ['architecture','architecture.html','◈','Architecture Blueprint'],['settings','settings.html','⚙','Settings']
];

function renderShell(){
  const sidebar=document.getElementById('sidebar');
  if(!sidebar)return;
  sidebar.innerHTML=`<div class="brand"><div class="brand-mark"></div><div><h1>MEDICARE</h1><p>Infrastructure Command Center</p></div></div><p class="nav-label">COMMAND CENTER</p><nav class="nav">${navItems.map(([id,url,icon,label])=>`<a href="${url}" class="${page===id?'active':''}"><span class="nav-icon">${icon}</span>${label}</a>`).join('')}</nav><div class="sidebar-bottom"><p class="system-label">SYSTEM STATUS</p><div class="system-box"><span class="dot pulse"></span>All Systems Operational</div><div class="admin"><div class="avatar">IA</div><div><strong>Infrastructure Admin</strong><span>System Administrator</span></div></div></div>`;
}
function initGlobal(){
  renderShell();
  const sidebar=document.getElementById('sidebar'), overlay=document.querySelector('.mobile-overlay');
  document.querySelector('.menu-btn')?.addEventListener('click',()=>{sidebar?.classList.toggle('open');overlay?.classList.toggle('open')});
  overlay?.addEventListener('click',()=>{sidebar?.classList.remove('open');overlay.classList.remove('open')});
  document.querySelector('[data-theme-toggle]')?.addEventListener('click',()=>{const dark=document.documentElement.dataset.theme==='dark';document.documentElement.dataset.theme=dark?'light':'dark';localStorage.setItem('medicare-theme',dark?'light':'dark')});
  document.documentElement.dataset.theme=localStorage.getItem('medicare-theme')||'light';
  const notice=document.querySelector('.notification-panel');
  document.querySelector('[data-notifications]')?.addEventListener('click',(e)=>{e.stopPropagation();notice?.classList.toggle('open')});
  document.addEventListener('click',e=>{if(!notice?.contains(e.target))notice?.classList.remove('open')});
  document.querySelectorAll('[data-close-modal]').forEach(b=>b.addEventListener('click',()=>b.closest('.modal-backdrop')?.classList.remove('open')));
  document.querySelectorAll('.modal-backdrop').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('open')}));
}
function showModal(id){document.getElementById(id)?.classList.add('open')}
function toast(message,type='success'){const wrap=document.querySelector('.toast-wrap');if(!wrap)return;const el=document.createElement('div');el.className='toast';el.textContent=(type==='success'?'✓ ':'⚠ ')+message;wrap.append(el);setTimeout(()=>el.remove(),3500)}
function randomBars(container,count=16){if(!container)return;container.innerHTML=Array.from({length:count},()=>`<i style="--h:${25+Math.random()*70}%"></i>`).join('')}
function initDashboard(){
  document.querySelectorAll('.health-card').forEach(card=>card.addEventListener('click',()=>{document.getElementById('health-modal-title').textContent=card.dataset.title;document.getElementById('health-modal-content').innerHTML=`<p>${card.dataset.detail}</p><div class="score-item"><span>Current availability</span><strong>${card.dataset.value}</strong><div class="bar"><i style="--value:${card.dataset.bar}"></i></div></div>`;showModal('health-modal')}));
  setTimeout(()=>{const ring=document.querySelector('.score-ring');if(ring)ring.style.setProperty('--score','96%')},250);
  document.querySelectorAll('.sparkline').forEach(c=>randomBars(c,14));
  setInterval(()=>document.querySelectorAll('[data-live-metric]').forEach(el=>{const base=Number(el.dataset.liveMetric);const unit=el.dataset.unit||'%';const value=Math.max(1,base+Math.floor(Math.random()*7)-3);el.textContent=value+(unit==='%'?'%':` ${unit}`);el.dataset.liveMetric=String(value);randomBars(el.closest('.metric-card')?.querySelector('.sparkline'),14)}),4000);
}
function initInfrastructure(){
  const tabData={servers:['HMS-WEB-01','HMS-WEB-02','HMS-API-01','HMS-DB-01','HMS-TEST-01'],databases:['HMS-DB-01','HMS-DB-02','ANALYTICS-DB'],storage:['CLINICAL-STORE','BACKUP-VAULT','ARCHIVE-TIER'],network:['CORE-LB-01','HOSPITAL-VPN','EDGE-GATEWAY']};
  document.querySelectorAll('.tab').forEach(tab=>tab.addEventListener('click',()=>{document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));tab.classList.add('active');const type=tab.dataset.tab;document.querySelectorAll('[data-resource-row]').forEach((row,i)=>{const names=tabData[type];row.style.display=i<names.length?'table-row':'none';if(i<names.length)row.querySelector('.resource-name').textContent=names[i]});}));
  document.querySelector('[data-open-provision]')?.addEventListener('click',()=>showModal('provision-modal'));
  document.querySelector('[data-provision]')?.addEventListener('click',()=>{
    const p=document.querySelector('#provision-modal .progress span'),label=document.querySelector('#provision-modal .progress-label');
    let val=0;
    document.querySelector('#provision-modal .form-grid').style.display='none';
    document.querySelector('#provision-modal .simulation').style.display='block';
    const timer=setInterval(()=>{
      val+=10;p.style.width=val+'%';label.textContent=val+'%';
      if(val>=100){
        clearInterval(timer);
        label.textContent='Resource provisioned successfully';
        toast('Resource provisioned successfully');
        if(window.location.protocol.startsWith('http')){
          fetch('/api/provision',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({resource_type:'Virtual Machine Node',environment:'Development',region:'Chennai Data Center'})
          }).catch(()=>{});
        }
      }
    },180);
  });
}
function initDeployments(){
  const start=()=>{showModal('deploy-modal');const confirm=document.querySelector('#deploy-modal .confirm-view'),sim=document.querySelector('#deploy-modal .simulation');confirm.style.display='block';sim.style.display='none'};
  document.querySelector('[data-open-deploy]')?.addEventListener('click',start);
  document.querySelector('[data-confirm-deploy]')?.addEventListener('click',()=>{
    const confirm=document.querySelector('#deploy-modal .confirm-view'),sim=document.querySelector('#deploy-modal .simulation'),bar=sim.querySelector('.progress span'),label=sim.querySelector('.progress-label'),stages=[...sim.querySelectorAll('.stage')];
    confirm.style.display='none';sim.style.display='block';
    let step=0;
    const timer=setInterval(()=>{
      step++;const val=Math.min(step*25,100);
      bar.style.width=val+'%';label.textContent=val+'%';
      stages.slice(0,Math.ceil(val/17)).forEach(s=>{s.classList.add('done');s.querySelector('span').textContent='✓'});
      if(val===100){
        clearInterval(timer);
        label.textContent='Deployment Successful';
        toast('Deployment v2.4.2 completed successfully');
        if(window.location.protocol.startsWith('http')){
          fetch('/api/deploy',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({version:'v2.4.2',environment:'Production'})
          }).catch(()=>{});
        }
      }
    },650);
  });
  document.querySelectorAll('.filter-btn').forEach(btn=>btn.addEventListener('click',()=>{document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const f=btn.dataset.filter;document.querySelectorAll('[data-deployment-row]').forEach(r=>r.style.display=f==='all'||r.dataset.tags.includes(f)?'table-row':'none')}));
}
function initMonitoring(){document.querySelectorAll('.line-chart').forEach(c=>randomBars(c,24));setInterval(()=>{document.querySelectorAll('[data-monitor]').forEach(el=>{const v=Math.max(20,Math.min(89,Number(el.textContent.replace('%',''))+Math.floor(Math.random()*9)-4));el.textContent=v+'%';el.nextElementSibling?.querySelector('i')?.style.setProperty('--value',v+'%')});document.querySelectorAll('.line-chart').forEach(c=>randomBars(c,24))},3000)}
function initLogs(){const search=document.querySelector('[data-log-search]'),selects=[...document.querySelectorAll('[data-log-filter]')];const filter=()=>document.querySelectorAll('[data-log-row]').forEach(r=>{const q=(search?.value||'').toLowerCase();const text=r.textContent.toLowerCase();const matchQ=text.includes(q);const matchS=selects.every(s=>s.value==='all'||r.dataset[s.dataset.logFilter]===s.value);r.style.display=matchQ&&matchS?'table-row':'none'});search?.addEventListener('input',filter);selects.forEach(s=>s.addEventListener('change',filter))}
function initSettings(){document.querySelector('[data-save-settings]')?.addEventListener('click',()=>toast('Settings saved successfully'))}
document.addEventListener('DOMContentLoaded',()=>{initGlobal();({dashboard:initDashboard,infrastructure:initInfrastructure,deployments:initDeployments,monitoring:initMonitoring,logs:initLogs,settings:initSettings}[page]||(()=>{}))()});
