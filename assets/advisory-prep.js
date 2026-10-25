"use strict";
(() => {
  const form = document.getElementById("advisory-prep");
  if (!form) return;
  form.addEventListener("submit", event => {
    event.preventDefault();
    const fields = [["prep-profit", "Annual business profit"], ["prep-income", "Household income"], ["prep-entities", "Business entities"], ["prep-properties", "Investment properties"], ["prep-decision", "Main decision"], ["prep-timing", "Timing"], ["prep-investment", "Advisory investment"]];
    const lines = fields.map(([id, label]) => {
      const value = document.getElementById(id).value;
      return value ? label + ": " + value : "";
    }).filter(Boolean);
    document.getElementById("prep-summary").value = lines.join("\n");
    document.getElementById("prep-status").textContent = lines.length ? "Summary ready. Copy it for your call; it has not been sent to AE." : "Choose at least one answer to prepare a summary. You can also book directly below.";
  });
})();
