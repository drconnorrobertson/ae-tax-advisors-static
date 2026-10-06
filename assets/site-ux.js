(() => {
  if (document.documentElement.dataset.aeSharedUxReady) return;
  document.documentElement.dataset.aeSharedUxReady = 'true';
  const main = document.querySelector('main');
  if (main) {
    main.id = main.id || 'main-content';
    if (!main.hasAttribute('tabindex')) main.tabIndex = -1;
    if (!document.querySelector('.skip-link')) {
      const skip = document.createElement('a');
      skip.className = 'skip-link'; skip.href = '#' + main.id;
      skip.textContent = 'Skip to main content';
      document.body.prepend(skip);
    }
  }

  // Keep wide data tables inside a keyboard-accessible scrolling region.
  function prepareTables() {
    document.querySelectorAll('main table').forEach((table) => {
      let wrapper = table.parentElement;
      if (!wrapper.classList.contains('ae-table-scroll')) {
        const style = getComputedStyle(wrapper);
        if (['auto', 'scroll'].includes(style.overflowX)) {
          wrapper.classList.add('ae-table-scroll');
        } else {
        const region = document.createElement('div');
        region.className = 'ae-table-scroll';
        table.before(region); region.append(table); wrapper = region;
        }
      }
      if (wrapper.scrollWidth > wrapper.clientWidth + 1) {
        wrapper.tabIndex = 0; wrapper.setAttribute('role', 'region');
        const caption = table.querySelector('caption');
        wrapper.setAttribute('aria-label', caption ? caption.textContent.trim() : 'Scrollable data table');
      } else {
        wrapper.removeAttribute('tabindex'); wrapper.removeAttribute('role'); wrapper.removeAttribute('aria-label');
      }
    });
  }
  prepareTables();
  window.addEventListener('resize', prepareTables);
  document.addEventListener('ae:tool-complete', prepareTables);

  const menuButton = document.querySelector('.mobile-toggle');
  const menu = document.getElementById('primary-nav');
  if (!menuButton || !menu) return;

  const compactNavigation = window.matchMedia('(max-width: 1360px)');
  const groups = Array.from(menu.querySelectorAll('.nav-dropdown'));

  function closeMenu({ restoreFocus = false } = {}) {
    menu.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open menu');
    groups.forEach((group) => {
      group.classList.remove('submenu-open');
      const toggle = group.querySelector('.mobile-submenu-toggle');
      if (toggle) {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', toggle.getAttribute('aria-label').replace(/^Collapse /, 'Expand '));
        toggle.querySelector('span').textContent = '+';
      }
    });
    if (restoreFocus) menuButton.focus();
  }

  groups.forEach((group, index) => {
    const link = group.querySelector(':scope > .nav-link');
    const submenu = group.querySelector(':scope > .dropdown-content');
    if (!link || !submenu) return;

    const label = link.textContent.replace('▾', '').trim();
    const submenuId = `mobile-submenu-${index + 1}`;
    submenu.id = submenu.id || submenuId;

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'mobile-submenu-toggle';
    toggle.setAttribute('aria-controls', submenu.id);
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', `Expand ${label} menu`);
    toggle.innerHTML = '<span aria-hidden="true">+</span>';
    link.insertAdjacentElement('afterend', toggle);

    toggle.addEventListener('click', () => {
      const expanded = group.classList.toggle('submenu-open');
      toggle.setAttribute('aria-expanded', String(expanded));
      toggle.setAttribute('aria-label', `${expanded ? 'Collapse' : 'Expand'} ${label} menu`);
      toggle.querySelector('span').textContent = expanded ? '−' : '+';
    });
  });

  document.documentElement.classList.add('site-ux-ready');

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && compactNavigation.matches && menu.classList.contains('open')) {
      closeMenu({ restoreFocus: true });
    }
  });

  document.addEventListener('click', (event) => {
    if (compactNavigation.matches && menu.classList.contains('open') && !event.target.closest('header')) {
      closeMenu();
    }
  });

  compactNavigation.addEventListener('change', () => closeMenu());
})();

/* AE service scope: proactive planning, preparation, amendments and real estate. */
(function(){const excluded=new Set(["/ae-tax-advisors-vs-tax-relief-companies", "/blog/can-i-negotiate-with-the-irs-to-reduce-my-tax-debt", "/blog/first-time-penalty-abatement-irs", "/blog/innocent-spouse-relief-irc-6015", "/blog/offer-in-compromise-myths-reality", "/blog/unfiled-tax-returns-strategy", "/blog/what-is-irs-penalty-abatement-and-how-do-i-qualify", "/compare/pinnacle-tax-group-alternatives", "/irs-installment-agreement", "/irs-penalty-abatement", "/irs-tax-lien-vs-levy", "/offer-in-compromise-irs", "/tax-compliance-irs-representation", "/tax-resolution-services-2", "/unfiled-tax-returns-help"]);function applyScope(){document.querySelectorAll("a[href]").forEach(function(a){let u;try{u=new URL(a.getAttribute("href"),location.href);}catch(e){return;}if(u.origin===location.origin&&excluded.has(u.pathname.replace(/\/$/,""))){a.remove();}});}if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",applyScope,{once:true});}else{applyScope();}})();
