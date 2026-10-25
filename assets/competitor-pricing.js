(() => {
  const search = document.getElementById('provider-search');
  const evidence = document.getElementById('provider-evidence');
  const category = document.getElementById('provider-category');
  if (!search || !evidence || !category) return;
  const rows = [...document.querySelectorAll('#provider-rows tr')];
  function filter() {
    const query = search.value.toLowerCase().trim();
    let count = 0;
    for (const row of rows) {
      row.hidden = !row.dataset.provider.includes(query) ||
        (evidence.value !== '' && row.dataset.kind !== evidence.value) ||
        (category.value !== '' && row.dataset.category !== category.value);
      if (!row.hidden) count++;
    }
    document.getElementById('provider-count').textContent = count + (count === 1 ? ' provider' : ' providers');
  }
  search.addEventListener('input', filter);
  evidence.addEventListener('change', filter);
  category.addEventListener('change', filter);
})();
