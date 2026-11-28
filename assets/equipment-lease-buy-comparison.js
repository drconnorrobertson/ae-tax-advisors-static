'use strict';

const comparison = document.querySelector('#equipment-lease-buy-form');
if (comparison) {
  const dollars = new Intl.NumberFormat('en-US', {
    style: 'currency', currency: 'USD', maximumFractionDigits: 2
  });

  function update() {
    const output = comparison.querySelector('output');
    const inputNames = ['rate', 'leaseCash', 'leaseDeduction', 'buyCash', 'buyDeduction', 'resale', 'leaseResale'];
    const [rate, leaseCash, leaseDeduction, buyCash, buyDeduction, resale, leaseResale] =
      inputNames.map(name => comparison.elements.namedItem(name).valueAsNumber);
    if (!comparison.checkValidity() ||
        ![rate, leaseCash, leaseDeduction, buyCash, buyDeduction, resale, leaseResale].every(Number.isFinite)) {
      output.textContent = 'Enter a valid amount in every field. Use zero where an item does not apply.';
      return;
    }

    const leaseCostCents = Math.round((leaseCash - leaseDeduction * rate / 100 - leaseResale) * 100);
    const buyCostCents = Math.round((buyCash - buyDeduction * rate / 100 - resale) * 100);
    const difference = (leaseCostCents - buyCostCents) / 100;
    const comparisonText = difference === 0 ? 'The modeled costs are equal.' :
      (difference > 0 ? 'Buying' : 'Leasing') + ' costs ' + dollars.format(Math.abs(difference)) + ' less in this scenario.';
    output.textContent = 'Lease after tax: ' + dollars.format(leaseCostCents / 100) +
      '. Buy after tax: ' + dollars.format(buyCostCents / 100) + '. ' + comparisonText;
  }

  comparison.addEventListener('submit', event => event.preventDefault());
  comparison.addEventListener('input', update);
  comparison.querySelectorAll('[data-equipment-input]').forEach(input => {
    input.name = input.dataset.equipmentInput;
  });
  comparison.querySelector('[data-equipment-controls]').disabled = false;
  update();
}
