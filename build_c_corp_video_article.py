#!/usr/bin/env python3
"""Build the video-first C corporation decision guide from the supplied explainer."""

from pathlib import Path
import site_template as T

PATH = "/blog/c-corp-strategy-1m-business-owners/"
TITLE = "C Corp Strategy for $1M+ Owners: Reinvest or Distribute?"
DESCRIPTION = (
    "Watch the C corporation strategy explainer and compare retained earnings, "
    "dividends, reasonable compensation, and business reinvestment for high-profit owners."
)
DATE = "2026-09-27"
VIDEO = "/assets/videos/c-corp-strategy-for-1m-owners.mp4"
POSTER = "/assets/videos/c-corp-strategy-for-1m-owners-poster.webp"

CSS = """<style>
.video-guide-hero{padding:76px 24px 42px;background:var(--light-bg);text-align:center}
.video-guide-hero .container{max-width:920px}
.video-guide-eyebrow{display:block;color:#806126;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px}
.video-guide-hero h1{font-family:var(--font-heading);font-size:clamp(36px,5vw,62px);line-height:1.08;letter-spacing:-.035em;color:var(--dark);margin:18px 0}
.video-guide-hero p{font-size:18px;line-height:1.65;color:var(--medium);max-width:760px;margin:0 auto}
.video-guide-player-section{padding:0 24px 54px;background:var(--light-bg)}
.video-guide-player{max-width:1000px;margin:auto}
.video-guide-player video{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#071524;border-radius:12px;box-shadow:0 20px 45px rgba(7,23,30,.18)}
.video-guide-player figcaption{font-size:14px;line-height:1.6;color:var(--medium);margin-top:12px;text-align:center}
.video-guide-article{padding:58px 24px 76px}
.video-guide-article .container{max-width:800px}
.video-guide-article h2{font-size:clamp(27px,3vw,36px);line-height:1.2;margin:46px 0 16px}
.video-guide-article p,.video-guide-article li{font-size:17px;line-height:1.75}
.video-guide-article ul,.video-guide-article ol{padding-left:24px;margin:16px 0 24px}
.video-guide-article li+li{margin-top:8px}
.video-guide-article a{color:#24517d;text-decoration:underline;text-underline-offset:2px}
.video-guide-article a:hover{color:#806126}
.video-guide-summary{border-left:4px solid var(--accent);background:var(--light-bg);padding:22px 26px;margin:0 0 32px}
.video-guide-summary p{margin:0}
.video-guide-table-wrap{overflow-x:auto;margin:24px 0}
.video-guide-table{border-collapse:collapse;width:100%;min-width:560px;font-size:15px}
.video-guide-table th,.video-guide-table td{border:1px solid #d9e2eb;padding:12px 14px;text-align:left;vertical-align:top}
.video-guide-table th{background:var(--light-bg);color:var(--dark)}
.video-guide-chapters{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 24px;padding:0;list-style:none}
.video-guide-chapters li{margin:0!important}
.video-guide-chapters button{border:0;background:none;padding:4px 0;color:#24517d;font:inherit;text-align:left;text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.video-guide-chapters button:hover{color:#806126}
.video-guide-chapters button:focus-visible{outline:2px solid #806126;outline-offset:3px}
.video-guide-note{font-size:14px!important;color:var(--medium);border-top:1px solid #d9e2eb;padding-top:20px;margin-top:42px}
@media(max-width:640px){.video-guide-hero{padding:50px 18px 28px}.video-guide-hero p{font-size:16px}.video-guide-player-section{padding:0 12px 30px}.video-guide-player video{border-radius:6px}.video-guide-article{padding:35px 18px 55px}.video-guide-chapters{grid-template-columns:1fr}}
</style>"""

BODY = f"""
<section class="video-guide-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/blog/">Blog</a> &rsaquo; C Corp Strategy for $1M+ Owners</nav>
    <span class="video-guide-eyebrow">Video + decision guide</span>
    <h1>C Corp Strategy for $1M+ Owners: Reinvest or Distribute?</h1>
    <p>The 21% federal corporate rate can leave more after-tax cash inside a business for reinvestment. The owner’s eventual exit from that cash determines whether the structure works.</p>
  </div>
</section>
<section class="video-guide-player-section" aria-label="C corporation strategy video">
  <figure class="video-guide-player">
    <video controls playsinline preload="metadata" poster="{POSTER}" width="1280" height="720" aria-label="C Corp Strategy for one million dollar plus owners">
      <source src="{VIDEO}" type="video/mp4">
      Your browser cannot play this video. <a href="{VIDEO}">Open the MP4 file</a> instead.
    </video>
    <figcaption>3 minute 28 second explainer. The chapter outline and key points are available below the player.</figcaption>
  </figure>
</section>
<article class="video-guide-article">
  <div class="container">
    <div class="video-guide-summary"><p><strong>The decision:</strong> compare tax under the current entity with tax inside a C corporation, then model how and when the owner will use the money. The 21% corporate rate is one layer of that calculation, not the owner’s final tax rate.</p></div>
    <h2>Watch by topic</h2>
    <ul class="video-guide-chapters">
      <li><button type="button" data-video-time="5">0:05 — Pass-through versus C corporation</button></li>
      <li><button type="button" data-video-time="29">0:29 — Where retained capital can fit</button></li>
      <li><button type="button" data-video-time="49">0:49 — Why the corporate rate draws attention</button></li>
      <li><button type="button" data-video-time="75">1:15 — The $1 million illustration</button></li>
      <li><button type="button" data-video-time="99">1:39 — How money reaches the owner</button></li>
      <li><button type="button" data-video-time="121">2:01 — Four guardrails</button></li>
      <li><button type="button" data-video-time="148">2:28 — When a C corporation is a poor fit</button></li>
      <li><button type="button" data-video-time="171">2:51 — How to model the decision</button></li>
    </ul>

    <h2>Two paths for the next dollar of profit</h2>
    <p>In a pass-through business, taxable profit generally reaches the owner’s individual return even when cash stays in the business. A C corporation is a separate taxpayer. It can retain after-tax cash for corporate needs such as hiring, equipment, inventory, technology, or an acquisition. These differences matter most when a profitable owner has a real plan to keep and deploy capital inside the company.</p>
    <p>A C corporation is not automatically better at $1 million of revenue or profit. The right comparison uses actual taxable income, owner compensation, state taxes, planned distributions, and the expected holding period. See our broader <a href="/c-corporation-strategy/">C corporation strategy guide</a> and <a href="/c-corporation-strategy/c-corp-vs-s-corp/">C corporation versus S corporation analysis</a>.</p>

    <h2>What the $1 million example shows</h2>
    <p>The video uses a deliberately simplified, federal-only illustration: $1,000,000 of C corporation taxable income at a 21% rate produces $210,000 of federal corporate income tax and about $790,000 of after-tax corporate cash. It excludes state tax, deductions, credits, owner compensation, and other facts. <strong>It does not show $790,000 of tax-free personal cash.</strong></p>
    <div class="video-guide-table-wrap"><table class="video-guide-table"><caption class="sr-only">Simplified C corporation illustration</caption><thead><tr><th>Step</th><th>Illustrative amount</th><th>What it means</th></tr></thead><tbody>
      <tr><td>C corporation taxable income</td><td>$1,000,000</td><td>Assumed tax base, not revenue.</td></tr>
      <tr><td>Federal corporate income tax at 21%</td><td>$210,000</td><td>Corporate layer only.</td></tr>
      <tr><td>After-tax corporate cash</td><td>$790,000</td><td>Potentially available for corporate use before any shareholder-level tax.</td></tr>
    </tbody></table></div>
    <p>The IRS describes the federal corporate tax and the separate treatment of corporate distributions in <a href="https://www.irs.gov/publications/p542">Publication 542</a>. The actual result can differ materially from this illustration.</p>

    <h2>The exit question matters as much as the entry</h2>
    <p>Retaining cash postpones the shareholder distribution question while the funds remain in the business. Paying a dividend generally does not reduce the corporation’s taxable income and may create a shareholder tax. Paying reasonable salary or bonus can have different corporate, payroll, and individual tax effects. The IRS explains shareholder distribution treatment in <a href="https://www.irs.gov/taxtopics/tc404">Topic 404</a>.</p>
    <p>That is why a plan should model the complete path of the money: current operations, reinvestment, eventual distributions, and a possible sale. A lower first-layer rate can lose its advantage when the owner needs most profit for personal spending.</p>

    <h2>Four guardrails before retaining profits</h2>
    <ol>
      <li><strong>Business purpose:</strong> state why the corporation needs the capital, with an operating or acquisition plan.</li>
      <li><strong>Arm’s-length dealings:</strong> support related-party fees, loans, royalties, and services with real economics and records.</li>
      <li><strong>Accumulated earnings:</strong> assess whether retained earnings exceed the reasonable needs of the business. The IRS describes the potential tax in <a href="https://www.irs.gov/publications/p542">Publication 542</a>.</li>
      <li><strong>Documentation:</strong> keep budgets, board records, forecasts, contracts, and acquisition plans current.</li>
    </ol>
    <p>The structure may be a poor fit when the owner needs frequent personal distributions, has no supported reinvestment plan, or faces unfavorable state, industry, or exit economics.</p>

    <h2>A practical modeling sequence</h2>
    <ol>
      <li>Calculate business and owner-level tax under the current entity setup.</li>
      <li>Define how much capital the company can actually retain and deploy.</li>
      <li>Model salary, dividends, and eventual exit under the proposed structure.</li>
      <li>Refresh the business purpose, forecasts, and documentation annually.</li>
    </ol>
    <p>AE Tax Advisors can model these paths with your actual numbers before an election or restructuring. <a href="/discovery/">Book a call</a> to review the facts, or read the related guide on <a href="/blog/s-corp-to-c-corp-conversion-when-it-makes-sense/">when an S corporation to C corporation conversion can make sense</a>.</p>
    <p class="video-guide-note">Published September 27, 2026 by AE Tax Advisors. This article explains the accompanying video and is general information. Entity choice depends on the complete tax and legal facts of the business and its owners.</p>
  </div>
</article>
"""

SCHEMAS = [
    T.article_schema(
        title=TITLE, description=DESCRIPTION, url=T.SITE + PATH,
        published=DATE, modified=DATE, section="C-Corp Planning",
        keywords=["C corporation", "retained earnings", "business reinvestment", "high-profit owner"],
        citations=["https://www.irs.gov/publications/p542", "https://www.irs.gov/taxtopics/tc404"],
    ),
    {
        "@context": "https://schema.org", "@type": "VideoObject",
        "name": "C Corp Strategy for $1M+ Owners",
        "description": "How high-profit owners can evaluate a C corporation for reinvestment while managing double taxation and compliance risks.",
        "thumbnailUrl": T.SITE + POSTER,
        "uploadDate": DATE,
        "duration": "PT3M28S",
        "contentUrl": T.SITE + VIDEO,
        "publisher": {"@type": "Organization", "name": T.BRAND, "url": T.SITE + "/"},
    },
    T.breadcrumb_schema([("Home", "/"), ("Blog", "/blog/"), ("C Corp Strategy for $1M+ Owners", PATH)]),
]


def main() -> None:
    markup = T.build_page(
        title=TITLE, description=DESCRIPTION, path=PATH, body=BODY,
        schemas=SCHEMAS, published=DATE, modified=DATE,
        active_nav="/resources/", extra_head=CSS,
    )
    markup = markup.replace(
        f'<meta property="og:image" content="{T.SITE}/assets/ae-tax-logo.png">',
        f'<meta property="og:image" content="{T.SITE}{POSTER}">',
    ).replace(
        f'<meta name="twitter:image" content="{T.SITE}/assets/ae-tax-logo.png">',
        f'<meta name="twitter:image" content="{T.SITE}{POSTER}">',
    )
    markup = markup.replace("</body>", """<script>
document.querySelectorAll('[data-video-time]').forEach((button) => {
  button.addEventListener('click', () => {
    const player = document.querySelector('.video-guide-player video');
    if (!player) return;
    player.currentTime = Number(button.dataset.videoTime);
    player.scrollIntoView({behavior: 'smooth', block: 'center'});
    player.play().catch(() => {});
  });
});
</script>\n</body>""")
    out = T.write_page(PATH, markup)
    print(out)


if __name__ == "__main__":
    main()
