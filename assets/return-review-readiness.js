(function () {
  'use strict';
  const root = document.getElementById('return-readiness');
  if (!root) return;
  const button = document.getElementById('readiness-summary');
  const reset = document.getElementById('readiness-reset');
  const result = document.getElementById('readiness-result');
  const groups = Array.from(root.querySelectorAll('fieldset[data-topic]'));
  button.addEventListener('click', function () {
    result.replaceChildren();
    const items = groups.map(function (group) {
      const selected = group.querySelector('input:checked');
      return {topic: group.dataset.topic, value: selected ? selected.value : 'unanswered'};
    });
    const flagged = items.filter(function (item) { return ['review','unsure','unanswered'].includes(item.value); });
    const heading = document.createElement('h2');
    heading.textContent = flagged.length ? 'Topics to clarify before a review' : 'All topics marked confirmed or not applicable';
    result.append(heading);
    const list = document.createElement('ul');
    flagged.forEach(function (item) { const li = document.createElement('li'); li.textContent = item.topic + ': ' + ({review:'needs review',unsure:'unsure',unanswered:'not answered'}[item.value]); list.append(li); });
    result.append(list);
    const note = document.createElement('p');
    note.textContent = 'This is a discussion list, not a tax assessment, refund estimate or professional validation. No answers were submitted or saved.';
    result.append(note);
  });
  reset.addEventListener('click', function () { root.querySelectorAll('input').forEach(function (input) {input.checked = false;}); result.replaceChildren(); });
  button.disabled = false;
  reset.disabled = false;
}());
