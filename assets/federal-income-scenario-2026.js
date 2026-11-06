(function (root) {
  'use strict';
  // IRS Revenue Procedure 2025-32, sections 4.01 and 4.14. Tax year 2026 only.
  const brackets = {
    single: [12400, 50400, 105700, 201775, 256225, 640600],
    mfj: [24800, 100800, 211400, 403550, 512450, 768700],
    mfs: [12400, 50400, 105700, 201775, 256225, 384350],
    hoh: [17700, 67450, 105700, 201750, 256200, 640600]
  };
  const standard = {single:16100, mfj:32200, mfs:16100, hoh:24150};
  const rates = [.10,.12,.22,.24,.32,.35,.37];
  function amount(value, label) {
    if (typeof value !== 'number' || !Number.isFinite(value) || value < 0 || value > 1e12) throw new Error('Enter a nonnegative '+label+' no greater than $1 trillion.');
    return value;
  }
  function ordinaryTax(taxable, status) {
    amount(taxable, 'taxable income');
    if (!Object.hasOwn(brackets,status)) throw new Error('Choose a supported filing status.');
    let tax=0, lower=0;
    for (let i=0;i<rates.length;i++) {
      const upper=brackets[status][i] === undefined ? Infinity : brackets[status][i];
      tax += Math.max(0,Math.min(taxable,upper)-lower)*rates[i];
      if (taxable<=upper) break;
      lower=upper;
    }
    return tax;
  }
  function compare(input) {
    if (!Object.hasOwn(standard,input.status)) throw new Error('Choose a supported filing status.');
    const income=amount(input.income,'baseline income');
    const change=amount(input.change,'reviewed taxable-income reduction');
    if (!['standard','reviewed','taxable'].includes(input.mode)) throw new Error('Choose an income starting point.');
    const deduction=input.mode==='standard'?standard[input.status]:input.mode==='reviewed'?amount(input.deduction,'reviewed baseline deduction'):0;
    const baseline=Math.max(0,income-deduction), proposed=Math.max(0,baseline-change);
    const baselineTax=ordinaryTax(baseline,input.status), proposedTax=ordinaryTax(proposed,input.status);
    return {deduction,baseline,proposed,appliedReduction:baseline-proposed,unusedReduction:Math.max(0,change-baseline),baselineTax,proposedTax,difference:baselineTax-proposedTax};
  }
  if (typeof module!=='undefined'&&module.exports) module.exports={brackets,standard,ordinaryTax,compare};
  if (!root.document) return;
  const form=root.document.querySelector('[data-federal-scenario]');
  if (!form||form.dataset.initialized==='true') return;
  const installed=[];
  function listen(target,type,fn){target.addEventListener(type,fn);installed.push([target,type,fn]);}
  try {
    const byId=id=>root.document.getElementById(id), output=byId('federal-result'), error=byId('federal-error');
    const money=n=>new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',minimumFractionDigits:2,maximumFractionDigits:2}).format(n);
    const read=id=>{const value=byId(id).value.trim();return value===''?NaN:Number(value);};
    function clear(){output.hidden=true;error.textContent='';}
    function mode(){byId('federal-reviewed-wrap').hidden=byId('federal-mode').value!=='reviewed';clear();}
    listen(form,'submit',event=>{
      event.preventDefault();clear();
      try {
        if (!byId('federal-confirm').checked) throw new Error('Confirm that you understand the limited model before calculating.');
        const result=compare({status:byId('federal-status').value,mode:byId('federal-mode').value,income:read('federal-income'),deduction:read('federal-deduction'),change:read('federal-change')});
        const labels={deduction:'Baseline deduction subtracted by this tool',baseline:'Baseline taxable ordinary income',proposed:'Proposed taxable ordinary income',appliedReduction:'Taxable-income reduction applied',baselineTax:'Baseline federal ordinary income tax before credits',proposedTax:'Proposed federal ordinary income tax before credits',difference:'Illustrative federal income-tax difference'};
        const list=root.document.createElement('dl');
        for(const [key,label]of Object.entries(labels)){const term=root.document.createElement('dt');term.textContent=label;const value=root.document.createElement('dd');value.textContent=money(result[key]);list.append(term,value);}
        const note=root.document.createElement('p');note.textContent=result.unusedReduction>0?'The entered reduction exceeds baseline taxable income by '+money(result.unusedReduction)+'. This tool floors taxable income at zero; it does not determine an NOL, refund or carryover.':'This is a rate-table comparison, not a refund, total tax liability or confirmed strategy benefit.';
        output.replaceChildren(list,note);output.hidden=false;
      } catch(e){error.textContent=e.message;}
    });
    listen(form,'input',clear);listen(byId('federal-mode'),'change',mode);
    listen(form,'reset',()=>{clear();root.setTimeout(mode,0);});
    mode();form.querySelector('[data-local-controls]').disabled=false;form.querySelector('[type=submit]').disabled=false;
    byId('federal-ready').textContent='Ready. Calculations stay in this browser; inputs are not sent or saved by the tool.';
    form.dataset.initialized='true';
  } catch(error){installed.forEach(([target,type,fn])=>target.removeEventListener(type,fn));form.querySelector('[data-local-controls]').disabled=true;form.querySelector('[type=submit]').disabled=true;throw error;}
})(typeof window==='undefined'?globalThis:window);
