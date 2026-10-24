(function (root) {
  'use strict';
  function calculateSale(input) {
    const valid = (v, max = 1e12) => Number.isFinite(v) && v >= 0 && v <= max;
    for (const k of ['ordinaryRate', 'capitalRate', 'buildingRate', 'stateRate']) {
      const max = {ordinaryRate: 50, capitalRate: 20, buildingRate: 25, stateRate: 20}[k];
      if (!valid(input[k], max)) throw new Error('Enter a valid tax rate within the displayed range.');
    }
    if (input.buildingRate < Math.min(input.capitalRate, input.ordinaryRate)) throw new Error('The building-depreciation rate cannot be below both your ordinary and capital-gain rates. Review your rate assumptions.');
    if (!Array.isArray(input.assets) || input.assets.length !== 3 || input.assets.map(a => a.type).join(',') !== 'land,building,personal') throw new Error('Include land, building and Section 1245 assets separately.');
    let gain = 0, ordinary = 0, unrecaptured = 0, residual = 0, proceeds = 0, gross = 0, basis = 0;
    for (const a of input.assets) {
      if (![a.price, a.costs, a.basis, a.depreciation].every(v => valid(v))) throw new Error('Enter nonnegative amounts in every asset field.');
      if (a.costs > a.price) throw new Error('Selling costs cannot exceed allocated sale proceeds.');
      if (a.depreciation > a.basis) throw new Error('Depreciation cannot exceed pre-depreciation basis.');
      if (a.type === 'land' && a.depreciation !== 0) throw new Error('Land cannot have depreciation.');
      const net = a.price - a.costs, adjusted = a.basis - a.depreciation, g = net - adjusted;
      if (g < -0.005) throw new Error('An asset has a loss. This tool does not net asset losses or Section 1231 losses; request a return-level sale review.');
      const positive = Math.max(0, g);
      const recapture = a.type === 'personal' ? Math.min(positive, a.depreciation) : 0;
      const u1250 = a.type === 'building' ? Math.min(positive, a.depreciation) : 0;
      gross += a.price; proceeds += net; basis += adjusted; gain += positive; ordinary += recapture; unrecaptured += u1250; residual += positive - recapture - u1250;
    }
    if (gross <= 0) throw new Error('Enter sale proceeds for at least one asset.');
    if (!valid(input.debt) || input.debt > proceeds) throw new Error('Debt payoff must be between zero and net sale proceeds. Negative-equity sales require separate review.');
    const ordinaryTax = ordinary * input.ordinaryRate / 100;
    const buildingTax = unrecaptured * input.buildingRate / 100;
    const residualTax = residual * input.capitalRate / 100;
    const niit = input.niit ? gain * 0.038 : 0;
    const state = gain * input.stateRate / 100;
    const federal = ordinaryTax + buildingTax + residualTax + niit;
    const total = federal + state;
    return {gross, proceeds, basis, gain, ordinary, unrecaptured, residual, ordinaryTax, buildingTax, residualTax, niit, state, federal, total, cashBeforeTax: proceeds - input.debt, cashAfterTax: proceeds - input.debt - total};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {calculateSale};
  if (typeof document === 'undefined') return;
  const form = document.getElementById('rental-sale-form');
  if (!form) return;
  const output = document.getElementById('sale-output');
  const error = document.getElementById('sale-error');
  const money = n => new Intl.NumberFormat('en-US', {style:'currency',currency:'USD',maximumFractionDigits:0}).format(n);
  const read = id => { const value = document.getElementById(id).value.trim(); return value === '' ? NaN : Number(value); };
  function refresh(event) {
    if (event) event.preventDefault();
    output.hidden = true; error.textContent = '';
    if (!form.reportValidity()) return;
    if (!document.getElementById('sale-eligible').checked) { error.textContent = 'Confirm the model assumptions before calculating. For a sale outside those assumptions, request a review.'; return; }
    try {
      const input = {assets:['land','building','personal'].map(type => ({type,price:read(type+'-price'),costs:read(type+'-costs'),basis:read(type+'-basis'),depreciation:type === 'land' ? 0 : read(type+'-depreciation')})), ordinaryRate:read('ordinary-rate'),capitalRate:read('capital-rate'),buildingRate:read('building-rate'),stateRate:read('state-rate'),niit:document.getElementById('sale-niit').checked,debt:read('sale-debt')};
      const result = calculateSale(input);
      for (const [key,value] of Object.entries(result)) { const el = document.getElementById('result-'+key); if (el) el.textContent = money(value); }
      output.hidden = false;
      if (event) output.focus();
    } catch (e) { error.textContent = e.message; }
  }
  form.addEventListener('submit',refresh);
  form.addEventListener('input', () => { output.hidden = true; error.textContent = ''; });
  form.addEventListener('reset', () => { output.hidden = true; error.textContent = ''; });
  document.getElementById('sale-print').addEventListener('click', () => root.print());
})(typeof window === 'undefined' ? globalThis : window);
