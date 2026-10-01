(function (root) {
  'use strict';
  function compare(x) {
    if (!Number.isInteger(x.years) || x.years < 1 || x.years > 40) throw new Error('Choose a holding period from 1 to 40 whole years.');
    for (const key of ['fee', 'exitTax', 'discount']) {
      if (!Number.isFinite(x[key]) || x[key] < 0 || x[key] > (key === 'discount' ? 100 : 1e12)) throw new Error('Enter a valid ' + key + ' value.');
    }
    if (!Array.isArray(x.benefits) || x.benefits.length !== x.years || x.benefits.some(v => !Number.isFinite(v) || Math.abs(v) > 1e12)) throw new Error('Enter one signed tax cash-flow difference for each holding year.');
    const factor = 1 + x.discount / 100;
    const rows = x.benefits.map((benefit, i) => {
      const saleTax = i === x.years - 1 ? x.exitTax : 0;
      return { year: i + 1, benefit, saleTax, net: benefit - saleTax, presentValue: (benefit - saleTax) / Math.pow(factor, i + 1) };
    });
    return { rows, nominal: rows.reduce((s, r) => s + r.net, -x.fee), presentValue: rows.reduce((s, r) => s + r.presentValue, -x.fee) };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { compare };
  if (!root.document) return;
  const form = root.document.getElementById('holding-period-form');
  if (!form) return;
  const output = root.document.getElementById('holding-period-result');
  const money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  form.addEventListener('input', () => { output.textContent = 'Inputs changed. Compare again to update the result.'; });
  form.addEventListener('submit', event => {
    event.preventDefault();
    const value = key => form.elements[key].value.trim() === '' ? NaN : Number(form.elements[key].value);
    try {
      const tokens = form.elements.benefits.value.trim().split(/[\n,]/).map(v => v.trim());
      const result = compare({ years: value('years'), fee: value('fee'), exitTax: value('exitTax'), discount: value('discount'), benefits: tokens.map(v => v === '' ? NaN : Number(v)) });
      output.replaceChildren();
      const summary = root.document.createElement('p');
      summary.textContent = 'Net undiscounted difference after fee and entered sale tax: ' + money.format(result.nominal) + '. Net present value: ' + money.format(result.presentValue) + '.';
      const table = root.document.createElement('table'); table.className = 'blog-table';
      const caption = root.document.createElement('caption'); caption.textContent = 'Study versus no-study cash-flow differences from your inputs'; table.append(caption);
      const head = root.document.createElement('thead'); const row = root.document.createElement('tr');
      ['Year', 'Entered tax cash-flow difference', 'Entered additional sale tax', 'Net difference', 'Present value'].forEach(label => { const th = root.document.createElement('th'); th.scope = 'col'; th.textContent = label; row.append(th); });
      head.append(row); table.append(head);
      const body = root.document.createElement('tbody');
      result.rows.forEach(r => { const tr = root.document.createElement('tr'); [String(r.year), money.format(r.benefit), money.format(r.saleTax), money.format(r.net), money.format(r.presentValue)].forEach(v => { const td = root.document.createElement('td'); td.textContent = v; tr.append(td); }); body.append(tr); });
      table.append(body); const scroll = root.document.createElement('div'); scroll.className = 'ae-table-scroll'; scroll.append(table); output.append(summary, scroll);
      root.document.dispatchEvent(new CustomEvent('ae:tool-complete', { detail: { tool: 'holding_period' } }));
    } catch (error) { output.textContent = error.message; }
  });
})(typeof window !== 'undefined' ? window : globalThis);
