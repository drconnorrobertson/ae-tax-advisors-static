(() => {
  'use strict';
  const form = document.getElementById('route-form');
  if (!form) return;
  const current = location.pathname.includes('/book-connor-davis') ? 'connorDavis' : 'jacques';
  const error = document.getElementById('error');
  const params = new URLSearchParams(location.search);
  const allowed = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','gclid','fbclid','msclkid'];
  const attribution = new URLSearchParams();
  allowed.forEach(key => { if (params.has(key)) attribution.set(key, params.get(key)); });
  let configPromise;
  function config() {
    if (!configPromise) configPromise = fetch('/assets/ad-booking-config.json', {cache:'no-store'}).then(r => {
      if (!r.ok) throw new Error('Configuration unavailable');
      return r.json();
    });
    return configPromise;
  }
  function showPending() {
    document.getElementById('pending').hidden = false;
  }
  async function showBooking(answer) {
    form.hidden = true;
    const booking = document.getElementById('booking');
    booking.hidden = false;
    const calendar = document.getElementById('calendar');
    calendar.replaceChildren();
    document.getElementById('direct').hidden = true;
    document.getElementById('pending').hidden = true;
    booking.focus();
    try {
      const route = (await config())[current];
      // Use the supplied new calendars. The embedded GHL form saves the
      // business-owner answer; prefill only when its query mapping is verified.
      if (!route?.bookingUrl) return showPending();
      const url = new URL(route.bookingUrl);
      if (url.protocol !== 'https:' || !['api.leadconnectorhq.com','link.msgsndr.com','tax.aetaxadvisors.com'].includes(url.hostname)) return showPending();
      attribution.forEach((value,key) => url.searchParams.set(key,value));
      if (route.answerQueryKey) url.searchParams.set(route.answerQueryKey,answer === 'yes' ? 'Yes' : 'No');
      const iframe = document.createElement('iframe');
      iframe.src = url.href;
      iframe.title = 'Book with ' + (current === 'connorDavis' ? 'Connor Davis' : 'Jacques Snyman');
      iframe.id = 'ad-booking-calendar';
      iframe.allow = 'payment';
      iframe.setAttribute('scrolling', 'no');
      calendar.append(iframe);
      const link = document.createElement('a');
      link.href = url.href; link.target = '_blank'; link.rel = 'noopener';
      link.textContent = 'Open the booking calendar';
      const direct = document.getElementById('direct');
      direct.replaceChildren(link); direct.hidden = false;
      const script = document.createElement('script');
      script.src = 'https://link.msgsndr.com/js/form_embed.js';
      script.defer = true; document.body.append(script);
    } catch { showPending(); }
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    error.textContent = '';
    const answer = new FormData(form).get('business_owner');
    if (!['yes','no'].includes(answer)) { error.textContent = 'Please select Yes or No.'; return; }
    const destination = answer === 'yes' ? 'connorDavis' : 'jacques';
    if (destination !== current) {
      const query = new URLSearchParams(attribution);
      query.set('business_owner', answer);
      const destinationPath = destination === 'connorDavis' ? '/book-connor-davis/' : '/book-jacques/';
      location.assign(destinationPath + '?' + query.toString());
    } else showBooking(answer);
  });
  document.getElementById('change').addEventListener('click', () => {
    document.getElementById('booking').hidden = true;
    document.getElementById('calendar').replaceChildren();
    form.hidden = false;
    form.querySelector('input').focus();
    const clean = new URL(location.href); clean.searchParams.delete('business_owner');
    history.replaceState(null, '', clean);
  });
  // Query data only preselects the question. The visitor confirms before booking.
  const selected = params.get('business_owner');
  if (['yes','no'].includes(selected)) form.querySelector('input[value="'+selected+'"]').checked = true;
})();
