(function(){
'use strict';
var grid=document.getElementById('cs-grid');if(!grid)return;
var cards=Array.from(grid.querySelectorAll('.cs-card')),chips=Array.from(document.querySelectorAll('.cs-filters .cs-chip'));
var search=document.getElementById('cs-search'),count=document.getElementById('cs-count'),empty=document.getElementById('cs-empty'),more=document.getElementById('cs-more');
var fields={income:document.getElementById('cs-income'),ownership:document.getElementById('cs-ownership'),estate:document.getElementById('cs-estate')};
var shown=48,category='all',params=new URLSearchParams(location.search);
Object.keys(fields).forEach(function(k){var v=params.get(k);if(v&&Array.from(fields[k].options).some(function(o){return o.value===v;}))fields[k].value=v;});
search.value=params.get('q')||'';
if(chips.some(function(c){return c.dataset.cat===params.get('category');}))category=params.get('category');
function render(){
 var q=search.value.trim().toLowerCase(),n=0,visible=0;
 cards.forEach(function(c){var match=(category==='all'||c.dataset.cat===category)&&Object.keys(fields).every(function(k){return fields[k].value==='all'||fields[k].value===c.dataset[k];})&&(!q||(c.dataset.text+' '+c.textContent).toLowerCase().includes(q));
 if(match)n++;c.hidden=!match||n>shown;c.style.display=c.hidden?'none':'';if(!c.hidden)visible++;});
 count.textContent=n+(n===1?' matching case study':' matching case studies')+' · '+cards.length+' in the library';
 empty.style.display=n===0?'block':'none';more.style.display=n>visible?'':'none';
 chips.forEach(function(c){c.setAttribute('aria-pressed',String(c.dataset.cat===category));});
 var url=new URL(location.href);['income','ownership','estate','q','category'].forEach(function(k){url.searchParams.delete(k);});
 Object.keys(fields).forEach(function(k){if(fields[k].value!=='all')url.searchParams.set(k,fields[k].value);});if(q)url.searchParams.set('q',search.value.trim());if(category!=='all')url.searchParams.set('category',category);
 history.replaceState(null,'',url.pathname+url.search+url.hash);
}
Object.keys(fields).forEach(function(k){fields[k].addEventListener('change',function(){shown=48;render();});});
chips.forEach(function(c){c.addEventListener('click',function(){category=c.dataset.cat;shown=48;render();});});
search.addEventListener('input',function(){shown=48;render();});more.addEventListener('click',function(){shown+=48;render();});
document.getElementById('cs-reset').addEventListener('click',function(){Object.keys(fields).forEach(function(k){fields[k].value='all';});search.value='';category='all';shown=48;render();});render();
})();
