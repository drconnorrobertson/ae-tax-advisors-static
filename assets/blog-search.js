/* Progressive enhancement: the static archive remains available without JavaScript. */
(function () {
  'use strict';
  function init() {
    var form = document.getElementById('blog-search-form');
    var input = document.getElementById('blog-search-input');
    var category = document.getElementById('blog-category');
    var grid = document.getElementById('blog-grid');
    var pagination = document.getElementById('blog-pagination');
    var status = document.getElementById('blog-result-status');
    var more = document.getElementById('blog-load-more');
    if (!form || !input || !category || !grid || !pagination || !status || !more || form.dataset.searchInitialized) return;
    form.dataset.searchInitialized = 'true';
    var originalNodes = Array.from(grid.childNodes);
    var originalStatus = status.textContent;
    var originalPaginationHidden = pagination.hidden;
    var index = null, pending = null, generation = 0, timer = null;
    var matches = [], shown = 0;
    var batchSize = 36;
    status.setAttribute('tabindex', '-1');

    function readURL() {
      var params = new URL(window.location.href).searchParams;
      input.value = params.get('q') || '';
      var value = params.get('category') || '';
      var option = Array.from(category.options).find(function (item) { return item.value.toLowerCase() === value.toLowerCase(); });
      if (!option && value) {
        option = document.createElement('option');
        option.value = value;
        option.textContent = value;
        category.appendChild(option);
      }
      category.value = option ? option.value : '';
    }
    function writeURL(mode) {
      var url = new URL(window.location.href);
      var query = input.value.trim();
      if (query) url.searchParams.set('q', query); else url.searchParams.delete('q');
      if (category.value) url.searchParams.set('category', category.value); else url.searchParams.delete('category');
      if (url.href !== window.location.href) window.history[mode + 'State'](null, '', url.href);
    }
    function restore() {
      grid.replaceChildren.apply(grid, originalNodes);
      pagination.hidden = originalPaginationHidden;
      more.hidden = true;
      status.textContent = originalStatus;
      grid.removeAttribute('aria-busy');
    }
    function validEntry(entry) {
      if (!entry || typeof entry.url !== 'string' || typeof entry.title !== 'string' || !entry.title.trim()) return null;
      try {
        var url = new URL(entry.url, window.location.origin);
        if (url.origin !== window.location.origin || !/^\/blog\/.+/.test(url.pathname) || url.username || url.password || url.search || url.hash || /[\\\u0000-\u0020]/.test(entry.url)) return null;
        return {
          url: url.pathname,
          title: entry.title,
          description: typeof entry.description === 'string' ? entry.description : '',
          category: typeof entry.category === 'string' ? entry.category : '',
          date: typeof entry.date === 'string' ? entry.date : ''
        };
      } catch (error) { return null; }
    }
    function loadIndex() {
      if (index) return Promise.resolve(index);
      if (!pending) {
        pending = fetch('/assets/blog-search-index.json', { credentials: 'same-origin' })
          .then(function (response) {
            if (!response.ok) throw new Error('Search index unavailable');
            return response.json();
          }).then(function (data) {
            if (!Array.isArray(data)) throw new Error('Invalid search index');
            var seen = new Set();
            index = data.map(validEntry).filter(function (entry) {
              if (!entry || seen.has(entry.url)) return false;
              seen.add(entry.url);
              return true;
            });
            return index;
          }).finally(function () { pending = null; });
      }
      return pending;
    }
    function element(tag, className, text) {
      var node = document.createElement(tag);
      node.className = className;
      node.textContent = text;
      return node;
    }
    function card(entry) {
      var article = element('article', 'blog-card', '');
      article.appendChild(element('span', 'blog-card-category', entry.category));
      var heading = element('h2', 'blog-card-title', '');
      var link = element('a', '', entry.title);
      link.href = entry.url;
      heading.appendChild(link);
      article.appendChild(heading);
      article.appendChild(element('p', 'blog-card-excerpt', entry.description));
      if (/^\d{4}-\d{2}-\d{2}$/.test(entry.date) && !isNaN(Date.parse(entry.date))) {
        var date = element('time', 'blog-card-date', new Date(entry.date + 'T00:00:00Z').toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' }));
        date.dateTime = entry.date;
        article.appendChild(date);
      }
      return article;
    }
    function appendBatch(moveFocus) {
      var end = Math.min(shown + batchSize, matches.length);
      var fragment = document.createDocumentFragment(), first;
      for (var i = shown; i < end; i += 1) {
        var node = card(matches[i]);
        if (!first) first = node.querySelector('a');
        fragment.appendChild(node);
      }
      grid.appendChild(fragment);
      shown = end;
      more.hidden = shown >= matches.length;
      status.textContent = matches.length ? 'Showing ' + shown + ' of ' + matches.length + ' matching article' + (matches.length === 1 ? '.' : 's.') : 'No articles match. Try another search or choose All categories.';
      if (moveFocus && first) first.focus();
    }
    function search(mode, focusResult) {
      clearTimeout(timer);
      var request = ++generation;
      if (mode) writeURL(mode);
      var query = input.value.trim().toLowerCase();
      var selectedCategory = category.value.toLowerCase();
      if (!query && !selectedCategory) {
        restore();
        if (focusResult) status.focus();
        return;
      }
      status.textContent = 'Loading article search…';
      grid.setAttribute('aria-busy', 'true');
      more.hidden = true;
      loadIndex().then(function (data) {
        if (request !== generation) return;
        var words = query.split(/\s+/).filter(Boolean);
        matches = data.filter(function (entry) {
          var text = (entry.title + ' ' + entry.description + ' ' + entry.category).toLowerCase();
          return (!selectedCategory || entry.category.toLowerCase() === selectedCategory) && words.every(function (word) { return text.includes(word); });
        });
        shown = 0;
        grid.replaceChildren();
        pagination.hidden = true;
        grid.removeAttribute('aria-busy');
        appendBatch(false);
        if (focusResult) status.focus();
      }).catch(function () {
        if (request !== generation) return;
        restore();
        status.textContent = 'Article search could not load. The archive and page links below still work. Submit your search again to retry.';
        if (focusResult) status.focus();
      });
    }
    input.addEventListener('input', function () {
      clearTimeout(timer);
      // Invalidate an in-flight response immediately, not after the debounce.
      generation += 1;
      timer = setTimeout(function () { search('replace', false); }, 200);
    });
    category.addEventListener('change', function () { search('push', false); });
    form.addEventListener('submit', function (event) { event.preventDefault(); search('push', true); });
    form.addEventListener('reset', function () {
      clearTimeout(timer);
      generation += 1;
      setTimeout(function () { input.value = ''; category.value = ''; search('push', false); input.focus(); }, 0);
    });
    more.addEventListener('click', function () { appendBatch(true); });
    window.addEventListener('popstate', function () { clearTimeout(timer); readURL(); search(null, false); });
    readURL();
    search(null, false);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
}());
