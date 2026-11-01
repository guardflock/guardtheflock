(function() {
  var body = document.body;
  var helpBtn = document.getElementById('help-now-btn');
  var exploreBtn = document.getElementById('explore-all-btn');
  var pathCards = document.querySelectorAll('.path-card');
  var casesShowBtn = document.getElementById('cases-show-btn');
  var caseWrapper = document.getElementById('case-content-wrapper');
  var casesGate = document.getElementById('cases-soft-gate');
  function activateTab(tabKey) {
    var btn = document.querySelector('.nav-tab[data-tab="' + tabKey + '"]');
    if (btn) btn.click();
  }
  function exitLanding(tabKey) {
    body.classList.remove('landing-mode');
    try { localStorage.setItem('gtf-seen-landing', '1'); } catch(e) {}
    if (tabKey) { activateTab(tabKey); window.scrollTo({ top: 0, behavior: 'smooth' }); }
  }
  pathCards.forEach(function(card) {
    card.addEventListener('click', function() { exitLanding(card.getAttribute('data-path')); });
  });
  if (exploreBtn) exploreBtn.addEventListener('click', function() { exitLanding('understand'); });
  if (helpBtn) helpBtn.addEventListener('click', function() {
    if (body.classList.contains('landing-mode')) exitLanding('respond');
    else {
      activateTab('respond');
      var panel = document.getElementById('tab-respond');
      if (panel) requestAnimationFrame(function() { panel.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
    }
  });
  if (casesShowBtn && caseWrapper) {
    casesShowBtn.addEventListener('click', function() {
      caseWrapper.classList.remove('hidden-cases');
      if (casesGate) casesGate.style.display = 'none';
      try { localStorage.setItem('gtf-cases-shown', '1'); } catch(e) {}
    });
    try {
      if (localStorage.getItem('gtf-cases-shown') === '1') {
        caseWrapper.classList.remove('hidden-cases');
        if (casesGate) casesGate.style.display = 'none';
      }
    } catch(e) {}
  }
  document.querySelectorAll('[data-goto]').forEach(function(el) {
    el.addEventListener('click', function() {
      var key = el.getAttribute('data-goto');
      if (body.classList.contains('landing-mode')) exitLanding(key);
      else activateTab(key);
    });
  });
  var hash = window.location.hash.slice(1);
  var skipLanding = false;
  if (hash) {
    var target = document.getElementById(hash);
    if (target) skipLanding = true;
  }
  try { if (localStorage.getItem('gtf-seen-landing') === '1') skipLanding = true; } catch(e) {}
  if (!skipLanding) {
    body.classList.add('landing-mode');
    document.querySelectorAll('.section').forEach(function(p) { p.classList.remove('active'); });
    document.querySelectorAll('.nav-tab').forEach(function(t) {
      t.classList.remove('active'); t.setAttribute('aria-selected', 'false');
    });
  } else {
    body.classList.remove('landing-mode');
  }
})();
