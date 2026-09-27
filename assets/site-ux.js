(() => {
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
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
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
