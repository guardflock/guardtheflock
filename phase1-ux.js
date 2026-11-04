(function() {
  var body=document.body,helpBtn=document.getElementById('help-now-btn');
  var exploreBtn=document.getElementById('explore-all-btn'),pathCards=document.querySelectorAll('.path-card');
  var startHereBtn=document.getElementById('start-here-btn'),layerBtn=document.getElementById('layer-deeper-btn');
  var deeper=document.getElementById('discern-deeper');
  function activateTab(key){var b=document.querySelector('.nav-tab[data-tab="'+key+'"]');if(b)b.click();}
  function exitLanding(key){body.classList.remove('landing-mode');try{localStorage.setItem('gtf-seen-landing','1');}catch(e){}if(key){activateTab(key);window.scrollTo({top:0,behavior:'smooth'});}}
  function showLanding(){body.classList.add('landing-mode');document.querySelectorAll('.section').forEach(p=>p.classList.remove('active'));document.querySelectorAll('.nav-tab[data-tab]').forEach(t=>{t.classList.remove('active');t.setAttribute('aria-selected','false');});window.scrollTo({top:0,behavior:'smooth'});}
  function revealDeeper(){if(!layerBtn||!deeper)return;layerBtn.setAttribute('aria-expanded','true');deeper.hidden=false;deeper.classList.remove('collapsed');try{localStorage.setItem('gtf-discern-deeper','1');}catch(e){}}
  function scrollTarget(target,id){requestAnimationFrame(()=>{target.scrollIntoView({behavior:'smooth',block:'start'});if(history.replaceState)history.replaceState(null,'','#'+id);});}
  pathCards.forEach(card=>card.addEventListener('click',()=>exitLanding(card.getAttribute('data-path'))));
  if(exploreBtn)exploreBtn.addEventListener('click',()=>exitLanding('understand'));
  if(startHereBtn)startHereBtn.addEventListener('click',showLanding);
  if(helpBtn)helpBtn.addEventListener('click',()=>{if(body.classList.contains('landing-mode'))exitLanding('respond');else{activateTab('respond');const panel=document.getElementById('tab-respond');if(panel)requestAnimationFrame(()=>panel.scrollIntoView({behavior:'smooth',block:'start'}));}});
  document.querySelectorAll('[data-goto]').forEach(el=>el.addEventListener('click',()=>{const key=el.getAttribute('data-goto');if(body.classList.contains('landing-mode'))exitLanding(key);else activateTab(key);}));
  if(layerBtn&&deeper){layerBtn.addEventListener('click',()=>{if(layerBtn.getAttribute('aria-expanded')==='true'){layerBtn.setAttribute('aria-expanded','false');deeper.hidden=true;deeper.classList.add('collapsed');try{localStorage.removeItem('gtf-discern-deeper');}catch(e){}}else revealDeeper();});try{if(localStorage.getItem('gtf-discern-deeper')==='1')revealDeeper();}catch(e){}}
  document.addEventListener('click',e=>{const link=e.target.closest&&e.target.closest('a[href^="#"]');if(!link)return;const id=link.getAttribute('href').slice(1),target=id&&document.getElementById(id);if(!target||!target.closest('#discern-deeper'))return;e.preventDefault();const panel=target.closest('.section[id^="tab-"]');if(panel){const key=panel.id.replace('tab-','');if(body.classList.contains('landing-mode'))exitLanding(key);else activateTab(key);}revealDeeper();scrollTarget(target,id);});
  const hash=window.location.hash.slice(1),hashTarget=hash&&document.getElementById(hash);let skipLanding=!!hashTarget;
  if(hashTarget&&hashTarget.closest('#discern-deeper'))revealDeeper();
  try{if(localStorage.getItem('gtf-seen-landing')==='1')skipLanding=true;}catch(e){}
  if(!skipLanding){body.classList.add('landing-mode');document.querySelectorAll('.section').forEach(p=>p.classList.remove('active'));document.querySelectorAll('.nav-tab[data-tab]').forEach(t=>{t.classList.remove('active');t.setAttribute('aria-selected','false');});}else body.classList.remove('landing-mode');
  window.gtfShowLanding=showLanding;window.gtfExitLanding=exitLanding;
})();