'use strict';
// Only standard AE headers need this enhancement. Preserve source and inline handlers.
function attribute(tag, name) {
  const match = tag.match(new RegExp('\\b' + name + '\\s*=\\s*(["\\\'])(.*?)\\1', 'i'));
  return match ? match[2] : '';
}
function ensureSharedUx(html) {
  const markup = html.replace(/<!--[\s\S]*?-->/g, '');
  const scripts = markup.match(/<script\b[^>]*>/gi) || [];
  if (scripts.some(tag => /^\/assets\/site-ux\.js(?:[?#]|$)/.test(attribute(tag, 'src')))) return html;
  const header = markup.match(/<header\b[^>]*>[\s\S]*?<\/header>/i);
  if (!header || !/<\/head\s*>/i.test(markup)) return html;
  const buttons = header[0].match(/<button\b[^>]*>/gi) || [];
  const navs = header[0].match(/<nav\b[^>]*>/gi) || [];
  if (!buttons.some(tag => attribute(tag, 'class').split(/\s+/).includes('mobile-toggle') && attribute(tag, 'aria-controls') === 'primary-nav')) return html;
  if (!navs.some(tag => attribute(tag, 'id') === 'primary-nav' && attribute(tag, 'class').split(/\s+/).includes('nav-links'))) return html;
  return html.replace(/<\/head\s*>/i, '<script defer src="/assets/site-ux.js" data-ae-navigation-only="true"></script>\n$&');
}
module.exports = {ensureSharedUx};
