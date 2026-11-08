// First-party event hooks. No personal data, query strings, cookies or remote loader.
(() => {
  if (window.__aeBookingEventsReady) return;
  window.__aeBookingEventsReady = true;
  const safePath = value => /^\/[a-z0-9/_.-]*$/i.test(value) ? value : '/';
  // Stable content groups for the existing, first-party analytics integration.
  const contentGroup = pathname => {
    if (/solar/.test(pathname)) return 'solar-investment';
    if (/equipment.*(leas|invest)|heavy-equipment/.test(pathname)) return 'equipment-investment';
    if (/^\/compare\//.test(pathname)) return 'provider-comparisons';
    if (/str-|short-term|airbnb/.test(pathname)) return 'short-term-rental';
    if (/cost-seg|bonus-depreciation|macrs/.test(pathname)) return 'cost-segregation-depreciation';
    if (/amend|1040/.test(pathname)) return 'amended-returns';
    if (/^\/workbooks\//.test(pathname)) return 'workbooks';
    return 'general-tax-planning';
  };
  const emit = (name, destination) => {
    const detail = {event:name,content_group:contentGroup(location.pathname),page_path:safePath(location.pathname),destination_host:destination.hostname,destination_path:safePath(destination.pathname)};
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(detail);
    document.dispatchEvent(new CustomEvent('ae:marketing-event',{detail}));
  };
  const calendar = url => url.protocol === 'https:' && url.hostname === 'api.leadconnectorhq.com' && /^\/widget\/booking\/[a-z0-9]+$/i.test(url.pathname);
  document.addEventListener('click', event => {
    const link = event.target.closest?.('a[href]');
    if (!link) return;
    try {
      const url = new URL(link.href,location.href);
      if (calendar(url)) emit('ae_calendar_open',url);
      else if (url.origin === location.origin && /^\/(discovery|cost-seg-discovery|book-connor-davis|book-jacques)\/?$/.test(url.pathname)) emit('ae_booking_cta_click',url);
    } catch {}
  },true);
  const seen = new WeakSet();
  const prepare = () => document.querySelectorAll('iframe[src]').forEach(frame => {
    if (seen.has(frame)) return;
    try {
      const url = new URL(frame.src,location.href);
      if (calendar(url)) {seen.add(frame);emit('ae_calendar_view',url);}
    } catch {}
  });
  prepare();
  new MutationObserver(records => {if(records.some(r => r.addedNodes.length)) prepare();}).observe(document.documentElement,{childList:true,subtree:true});
  // Completion is intentionally emitted only by the CRM's confirmed appointment
  // integration. Calendar views and iframe messages are not booked appointments.
})();
