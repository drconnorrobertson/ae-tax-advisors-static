/* Educational Section 461(l) arithmetic. No inputs are sent or stored. */
(function (root) {
  'use strict';
  const thresholds = Object.freeze({2025: {joint: 626000, other: 313000}, 2026: {joint: 512000, other: 256000}});
  function estimate({year, status, deductions, income}) {
    if (!thresholds[year] || !Object.hasOwn(thresholds[year], status)) throw new Error('Choose a supported tax year and filing status.');
    for (const value of [deductions, income]) if (typeof value !== 'number' || !Number.isFinite(value) || value < 0 || value > 1e12) throw new Error('Enter nonnegative dollar amounts up to 1 trillion.');
    const threshold = thresholds[year][status];
    const netLoss = Math.max(0, deductions - income);
    const deferred = Math.max(0, netLoss - threshold);
    return {threshold, netLoss, deferred, remainingLoss: netLoss - deferred};
  }
  if (typeof module === 'object' && module.exports) module.exports = {estimate, thresholds};
  if (!root.document) return;
  const form = root.document.querySelector('[data-ebl-form]');
  if (!form) return;
  const result = root.document.querySelector('[data-ebl-result]');
  const error = root.document.querySelector('[data-ebl-error]');
  const currency = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD', maximumFractionDigits: 0});
  form.addEventListener('submit', function (event) {
    event.preventDefault(); error.textContent = ''; result.hidden = true;
    try {
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const data = new FormData(form);
      const values = estimate({year: data.get('year'), status: data.get('status'), deductions: Number(data.get('deductions')), income: Number(data.get('income'))});
      for (const [key, value] of Object.entries(values)) result.querySelector('[data-ebl-value="' + key + '"]').textContent = currency.format(value);
      result.querySelector('[data-ebl-summary]').textContent = values.netLoss === 0 ? 'These inputs produce no aggregate net business loss, so this simplified calculation produces no excess business loss.' : values.deferred === 0 ? 'The aggregate net loss is within the selected threshold. Section 461(l) produces no deferral in this simplified calculation.' : 'The amount above the selected threshold is deferred under this simplified Section 461(l) calculation. It is not a current-year tax saving.';
      result.hidden = false; result.focus();
    } catch (e) { error.textContent = e.message; }
  });
  form.addEventListener('reset', function () { result.hidden = true; error.textContent = ''; });
  form.querySelector('button[type=submit]').disabled = false;
})(typeof window === 'undefined' ? globalThis : window);
