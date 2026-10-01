// Integration hooks only: no remote endpoint, cookies, storage or financial inputs.
(() => {
  function publish(name, resource) {
    const detail = { event: name, resource, page_path: window.location.pathname };
    document.dispatchEvent(new CustomEvent('ae:marketing-event', { detail }));
    if (Array.isArray(window.dataLayer)) window.dataLayer.push(detail);
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('a[data-ae-resource]');
    if (link) publish(link.hasAttribute('download') ? 'ae_resource_download' : 'ae_consultation_click', link.dataset.aeResource);
  });
  document.addEventListener('ae:tool-complete', event => {
    if (event.detail && event.detail.tool === 'holding_period') publish('ae_tool_complete', 'holding_period');
  });
})();
