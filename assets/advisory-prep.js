"use strict";
(() => {
  const form = document.getElementById("advisory-prep");
  if (!form) return;
  const el = id => document.getElementById(id);
  const money = value => value.toLocaleString("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 });
  const fields = [["prep-profit", "Annual business profit"], ["prep-income", "Household income"], ["prep-entities", "Business entities"], ["prep-properties", "Investment properties"], ["prep-decision", "Main decision"], ["prep-timing", "Timing"], ["prep-investment", "Advisory investment"]];
  function calculate() {
    const tax = Number(el("prep-tax").value);
    const low = Number(el("prep-low").value);
    const high = Number(el("prep-high").value);
    el("prep-high").setCustomValidity("");
    const valid = ["prep-tax", "prep-low", "prep-high"].every(id => el(id).value.trim() !== "" && el(id).validity.valid) && [tax, low, high].every(Number.isFinite) && tax >= 0 && tax <= 100000000 && low >= 0 && high <= 100 && low <= high;
    if (low > high) el("prep-high").setCustomValidity("The upper percentage must be at least the lower percentage.");
    const lines = fields.map(([id, label]) => el(id).value ? label + ": " + el(id).value : "").filter(Boolean);
    let result = "Savings estimate: not calculated. Annual federal tax and valid scenario percentages are needed.";
    el("prep-estimate").textContent = el("prep-tax").value === "" ? "Enter your annual federal income tax to see a scenario." : "Check your tax amount and scenario percentages.";
    el("prep-math").textContent = "";
    if (valid) {
      const range = money(tax * low / 100) + " to " + money(tax * high / 100);
      el("prep-estimate").textContent = range + " per year";
      el("prep-math").textContent = money(tax) + " annual federal income tax × " + low + "% to " + high + "% assumed reduction. Before fees and costs.";
      result = "Illustrative annual tax savings: " + range + ".\nCalculation: " + money(tax) + " annual federal income tax × " + low + "% to " + high + "% assumed reduction.\nAssumptions only, not an AE client average or prediction. Actual savings may be $0. Before fees, implementation costs and required spending/contributions. Timing benefits may reverse.";
    }
    const topics = [];
    if (el("prep-profit").value && !["No current business profit", "Prefer to discuss"].includes(el("prep-profit").value)) topics.push("Review owner compensation, entity structure and deductible business expenses.");
    if (el("prep-properties").value && el("prep-properties").value !== "None") topics.push("Review depreciation, cost segregation and rental loss eligibility; property ownership alone does not establish usable deductions.");
    if (["2–3", "4 or more"].includes(el("prep-entities").value)) topics.push("Coordinate entity filings and intercompany activity.");
    if (el("prep-decision").value) topics.push("Discuss: " + el("prep-decision").value + ".");
    el("prep-summary").value = [result, ...lines, topics.length ? "Topics to evaluate (eligibility not established):\n" + topics.join("\n") : "", "Strategic advisory: $7,800; complex advisory: $9,800. Additional services separately scoped.", "Not sent to AE. Copy this summary for your call."].filter(Boolean).join("\n\n");
    el("prep-copy").hidden = false;
    return valid;
  }
  form.addEventListener("input", () => { calculate(); el("prep-status").textContent = "Summary updated. These answers have not been sent to AE."; });
  form.addEventListener("change", calculate);
  form.addEventListener("submit", event => {
    event.preventDefault();
    const valid = calculate();
    el("prep-status").textContent = valid ? "Savings scenario and summary ready. Copy them for your call; they have not been sent to AE." : "Summary ready. Add annual federal tax and valid percentages to include a savings scenario, or book directly below.";
  });
  el("prep-copy").addEventListener("click", async () => {
    calculate();
    try {
      await navigator.clipboard.writeText(el("prep-summary").value);
      el("prep-status").textContent = "Summary copied. Paste it into your notes for the call.";
    } catch {
      el("prep-summary").focus();
      el("prep-summary").select();
      el("prep-status").textContent = "Select and copy the summary above. Automatic copying is unavailable in this browser.";
    }
  });
})();
