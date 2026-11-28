'use strict';

const feet = document.getElementById('cost-segregation-fee-square-feet');
const feeOutput = document.getElementById('cost-segregation-fee-result');

if (feet && feeOutput) {
  const dollars = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  feet.addEventListener('input', () => {
    if (feet.value === '') {
      feeOutput.textContent = 'Enter the billable square footage to see an estimate.';
      return;
    }
    if (!feet.validity.valid || !Number.isFinite(feet.valueAsNumber)) {
      feeOutput.textContent = 'Enter a whole number from 1 to 10,000,000 square feet.';
      return;
    }
    const estimate = Math.max(2000, feet.valueAsNumber);
    feeOutput.textContent = 'Illustrative standard study fee: ' + dollars.format(estimate) +
      (feet.valueAsNumber <= 2000 ? ' (the $2,000 minimum applies).' : '.');
  });
  feet.disabled = false;
}
