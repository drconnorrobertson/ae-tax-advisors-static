'use strict';
// Only standard AE headers need this enhancement. Preserve source and inline handlers.
function attribute(tag, name) {
  const match = tag.match(new RegExp('\\b' + name + '\\s*=\\s*(["\\\'])(.*?)\\1', 'i'));
  return match ? match[2] : '';
}
function ensureSharedUx(html) {
  const markup = html.replace(/<!--[\s\S]*?-->/g, '');
  const header = markup.match(/<header\b[^>]*>[\s\S]*?<\/header>/i);
  if (!header || !/<\/head\s*>/i.test(markup)) return html;
  const buttons = header[0].match(/<button\b[^>]*>/gi) || [];
  const navs = header[0].match(/<nav\b[^>]*>/gi) || [];
  if (!navs.some(tag => attribute(tag, 'id') === 'primary-nav' && attribute(tag, 'class').split(/\s+/).includes('nav-links'))) return html;
  const updated = html.replace(/<nav\b[^>]*>[\s\S]*?<\/nav>/gi, (nav) => {
    if (attribute(nav.match(/^<nav\b[^>]*>/i)[0], 'id') !== 'primary-nav') return nav;
    return nav.replace(/<a\b[^>]*>\s*Cost Segregation\s*<span\b/gi, (link) => {
      const tag = link.match(/^<a\b[^>]*>/i)[0];
      if (!attribute(tag, 'class').split(/\s+/).includes('nav-link') ||
          attribute(tag, 'href') !== '/cost-segregation-airbnb/') return link;
      return link.replace(/(\bhref\s*=\s*)(["'])(\/cost-segregation-airbnb\/)\2/i,
        (_, prefix, quote) => prefix + quote + '/cost-segregation-study/' + quote);
    });
  });
  if (!buttons.some(tag => attribute(tag, 'class').split(/\s+/).includes('mobile-toggle') && attribute(tag, 'aria-controls') === 'primary-nav')) return updated;
  const scripts = markup.match(/<script\b[^>]*>/gi) || [];
  if (scripts.some(tag => /^\/assets\/site-ux\.js(?:[?#]|$)/.test(attribute(tag, 'src')))) return updated;
  return updated.replace(/<\/head\s*>/i, '<script defer src="/assets/site-ux.js" data-ae-navigation-only="true"></script>\n$&');
}
module.exports = {ensureSharedUx};
