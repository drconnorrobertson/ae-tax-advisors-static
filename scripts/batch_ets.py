"""Batch: final comparison page referenced from the compare hub."""

from blog_gen import write_all

ARTICLES = [{
"slug": "compare/engineered-tax-services-vs-ae-tax",
"standalone": True,
"crumb_name": "Compare", "crumb_path": "compare",
"title": "Engineered Tax Services vs AE Tax Advisors",
"meta_title": "Engineered Tax Services vs AE Tax Advisors (2026) | AE Tax Advisors",
"meta_desc": "ETS is a specialty study provider. AE Tax pairs the engineering study with the tax planning that determines whether you can actually use the deduction.",
"category": "Comparison", "date": "2026-08-11",
"intro": [
"Engineered Tax Services is a well established specialty tax firm known for engineering-based cost segregation studies, energy incentive work under IRC Sec. 179D and Sec. 45L, and research credit studies.",
"The comparison worth making is not about study quality. It is about what happens on either side of the study, because a study is only worth what you can actually deduct.",
],
"sections": [
("What a Specialty Study Provider Does", [
"A specialty provider performs the engineering analysis: quantity takeoffs, component identification, cost allocation, and a report assigning each asset a recovery period with supporting authority.",
"That work is real and it matters. The IRS Cost Segregation Audit Techniques Guide identifies the detailed engineering approach as the most reliable, and it requires people who understand construction as well as tax classification.",
"What a study provider generally does not do is prepare your return, determine whether the resulting loss is deductible, evaluate your entity structure, or decide which tax year the deduction should land in.",
"Those questions are frequently worth more than the difference between a 24% and a 27% reclassification.",
]),
("The Questions the Study Does Not Answer", [
"Can you use the loss? Under IRC Sec. 469 a rental loss is passive by default. Without real estate professional status, a short-term rental under the seven-day rule, or passive income to absorb it, a $300,000 deduction suspends and produces nothing currently.",
"Does your entity cap it? An S corporation shareholder receives no basis for entity-level debt under IRC Sec. 1366(d), which can limit the deductible loss well below the study result. An LLC taxed as a partnership does not have this problem.",
"Which year should it land in? A look-back study filed with Form 3115 places the entire catch-up as a Sec. 481(a) adjustment in a year you choose. Running the study in a low-income year wastes it.",
"What does your state do? California and Massachusetts do not conform to bonus depreciation at all. New York and New Jersey require addbacks. North Carolina requires an 85% addback recovered over five years. The federal number alone is misleading in those states.",
"Is a study even worthwhile? Below roughly $400,000 of depreciable basis on residential property, or with a two-year hold where recapture reverses the benefit, the answer is sometimes no.",
]),
("How the Two Models Differ in Practice", [
"With a specialty provider, you engage them for the study, receive the report, and hand it to your CPA to implement. That works well when your CPA is already handling the surrounding analysis competently.",
"It works less well when nobody owns the questions above. The common outcome is an accurate study producing a suspended loss, or a study run in the wrong year, or a deduction implemented without the aggregation election under Treasury Regulation Sec. 1.469-9(g) that would have made it usable.",
"With an integrated firm, the study and the tax analysis are done by the same people. The order of operations is reversed: the loss exit and entity structure are resolved first, then the study is commissioned into the year where it works.",
]),
("Where AE Tax Advisors Fits", [
"We perform cost segregation studies with engineering support and produce a full component listing with authority cited for each classification, because a study you cannot defend is worse than no study.",
"We also do the planning and the compliance, so the passive activity analysis, the entity review, the state modeling, and the Form 3115 filing all happen together.",
"Our engagements start with whether you can use the deduction, not with the property. For some clients that conversation ends with us recommending against a study this year and running it next year instead.",
"For energy incentive work under Sec. 179D and Sec. 45L, and for research credit studies, a dedicated specialty provider such as ETS is often the right choice, and we work alongside them where that fits.",
]),
("How to Choose", [
"If you already have a tax advisor who is actively managing your passive activity position, entity structure, and multi-year timing, a specialty study provider slots in cleanly and does excellent work.",
"If nobody is currently answering the questions in the second section above, buying a study first is solving the wrong problem in the wrong order.",
"If you need Sec. 179D, Sec. 45L, or research credit work specifically, a specialty firm with that practice depth is generally the better fit.",
"Either way, ask any provider for a sample report and confirm it includes a complete asset listing with recovery periods and cited authority, a documented methodology, and a reconciliation to total depreciable basis.",
]),
],
"faqs": [
("Is Engineered Tax Services a good cost segregation provider?",
 "ETS is an established specialty firm doing engineering-based studies along with Sec. 179D, Sec. 45L, and research credit work. The comparison worth making is not study quality but who is answering the surrounding tax questions that determine whether you can use the deduction."),
("What does a study provider not do?",
 "Generally they do not prepare your return, determine whether the loss is deductible under IRC Sec. 469, evaluate whether your entity caps it under IRC Sec. 1366(d), choose the tax year for a Form 3115 catch-up, or model your state's conformity to bonus depreciation."),
("Why does the tax year of the study matter?",
 "A look-back study filed with Form 3115 places the entire cumulative catch-up in the year of filing as a Sec. 481(a) adjustment. Running it in a low-income year, or a year where the loss suspends, wastes deduction that could have offset a high-income year instead."),
("Should I use a specialty firm or an integrated one?",
 "If your advisor is already managing your passive activity position, entity structure, and timing, a specialty provider slots in well. If nobody is answering those questions, buying a study first solves the wrong problem in the wrong order."),
("What should any study report contain?",
 "A complete asset listing with cost allocations, recovery periods, and cited authority for each classification; a documented methodology; a reconciliation to total depreciable basis; and evidence of a physical inspection with photographs and drawings."),
],
"related": [
("/compare/kbkg-vs-ae-tax/", "KBKG vs AE Tax Advisors"),
("/compare/cssi-vs-ae-tax/", "CSSI vs AE Tax Advisors"),
("/blog/do-i-need-an-engineering-based-cost-segregation-study/", "Do you need an engineering based study"),
("/blog/how-to-evaluate-cost-segregation-study/", "How to evaluate a cost segregation study"),
],
"cta_head": "Resolve the Deduction Question First",
"cta_body": "Before commissioning any study, find out whether the loss will be usable in the year you take it. Send us your income picture, entity structure, and property detail.",
}]

if __name__ == "__main__":
    write_all(ARTICLES)
