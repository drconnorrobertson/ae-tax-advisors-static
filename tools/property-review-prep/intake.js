'use strict';
const form = document.querySelector('#intakeForm');
const summaryCard = document.querySelector('#summaryCard');
const summaryEl = document.querySelector('#summary');
let summaryText = '';
const labels = {
  property: 'Property', type: 'Property type', state: 'State', serviceDate: 'Placed in service',
  price: 'Purchase price', land: 'Estimated land value', improvements: 'Improvements',
  priorStudy: 'Prior cost seg study', depreciation: 'Depreciation started',
  advisor: 'Current tax advisor', questions: 'Questions'
};
const dollars = value => value ? new Intl.NumberFormat('en-US', {style:'currency', currency:'USD', maximumFractionDigits:0}).format(Number(value)) : 'Not provided';
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = Object.fromEntries(new FormData(form).entries());
  if (data.price && data.land && Number(data.land) > Number(data.price) + Number(data.improvements || 0)) {
    form.elements.land.setCustomValidity('Land value cannot exceed purchase price plus improvements.');
    form.elements.land.reportValidity();
    return;
  }
  const values = {...data, price:dollars(data.price), land:dollars(data.land), improvements:dollars(data.improvements)};
  summaryText = 'AE TAX ADVISORS — PROPERTY REVIEW PREP\nGenerated: ' + new Date().toLocaleDateString() + '\n\n' +
    Object.entries(labels).map(([key,label]) => label + ': ' + (values[key] || 'Not provided')).join('\n') +
    '\n\nDocuments to gather: closing statement, land allocation, improvement invoices, depreciation schedule, prior study if any.\n\nNo tax outcome or savings estimate has been calculated.';
  summaryEl.textContent = summaryText;
  summaryCard.hidden = false;
  summaryCard.scrollIntoView({behavior:'smooth', block:'start'});
});
for (const name of ['price', 'land', 'improvements']) {
  form.elements[name].addEventListener('input', () => form.elements.land.setCustomValidity(''));
}
form.addEventListener('reset', () => { summaryText = ''; summaryCard.hidden = true; form.elements.land.setCustomValidity(''); });
document.querySelector('#printBtn').addEventListener('click', () => window.print());
document.querySelector('#downloadBtn').addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([summaryText], {type:'text/plain'}));
  const a = document.createElement('a'); a.href = url; a.download = 'property-review-prep.txt'; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
