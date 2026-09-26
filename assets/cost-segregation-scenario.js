(function (root) {
  'use strict';
  function estimate(x) {
    const ranges = { price: [0, 1e12], land: [0, 100], reclass: [0, 100],
      month: [1, 12], rate: [0, 100], usable: [0, 100], fee: [0, 1e9] };
    for (const key of Object.keys(ranges)) {
      if (typeof x[key] !== 'number' || !Number.isFinite(x[key]) ||
          x[key] < ranges[key][0] || x[key] > ranges[key][1]) {
        throw new Error('Enter a valid ' + key + ' value.');
      }
    }
    if (![27.5, 39].includes(x.life) || !Number.isInteger(x.month)) {
      throw new Error('Choose a recovery period and a whole calendar month.');
    }
    if (!x.eligible) throw new Error('Confirm eligibility before estimating a 100% bonus scenario.');
    const basis = x.price * (1 - x.land / 100);
    const reclassified = basis * x.reclass / 100;
    const fraction = (12.5 - x.month) / 12;
    const without = basis / x.life * fraction;
    const withStudy = reclassified + (basis - reclassified) / x.life * fraction;
    const additional = withStudy - without;
    const currentlyUsable = additional * x.usable / 100;
    const benefit = currentlyUsable * x.rate / 100;
    return { basis, reclassified, without, withStudy, additional, currentlyUsable,
      benefit, net: benefit - x.fee };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { estimate };
  if (!root.document) return;
  const form = root.document.getElementById('cost-seg-scenario');
  if (!form) return;
  const output = root.document.getElementById('scenario-result');
  const money = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  form.addEventListener('input', function () { output.textContent = 'Inputs changed. Select Calculate to update the scenario.'; });
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const values = {};
    for (const key of ['price','land','reclass','life','month','rate','usable','fee']) {
      const raw = form.elements[key].value.trim();
      values[key] = raw === '' ? NaN : Number(raw);
    }
    values.eligible = form.elements.eligible.checked;
    try {
      const result = estimate(values);
      const labels = { basis: 'Depreciable basis in this scenario',
        reclassified: 'Assumed qualifying reclassified basis', without: 'First-year depreciation without study',
        withStudy: 'First-year depreciation with study', additional: 'Additional first-year deduction',
        currentlyUsable: 'Assumed currently usable additional deduction', benefit: 'Illustrative federal tax reduction',
        net: 'Illustrative current cash benefit after entered fee' };
      output.replaceChildren();
      const list = root.document.createElement('dl');
      for (const key of Object.keys(labels)) {
        const term = root.document.createElement('dt'); term.textContent = labels[key];
        const value = root.document.createElement('dd'); value.textContent = money.format(result[key]);
        list.append(term, value);
      }
      output.append(list);
    } catch (error) { output.textContent = error.message; }
  });
})(typeof window !== 'undefined' ? window : globalThis);
