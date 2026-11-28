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

    const leaseCost = leaseCash - leaseDeduction * rate / 100 - leaseResale;
    const buyCost = buyCash - buyDeduction * rate / 100 - resale;
    const difference = Math.round((leaseCost - buyCost) * 100) / 100;
    const comparisonText = difference === 0 ? 'The modeled costs are equal.' :
      (difference > 0 ? 'Buying' : 'Leasing') + ' costs ' + dollars.format(Math.abs(difference)) + ' less in this scenario.';
    output.textContent = 'Lease after tax: ' + dollars.format(leaseCost) +
      '. Buy after tax: ' + dollars.format(buyCost) + '. ' + comparisonText;
  }

  comparison.addEventListener('submit', event => event.preventDefault());
  comparison.addEventListener('input', update);
  update();
}
