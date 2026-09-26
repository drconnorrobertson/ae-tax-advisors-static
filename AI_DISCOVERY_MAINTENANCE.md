# AI discovery and access

AE's wildcard robots group allows public canonical content for existing and future search/retrieval agents. Do not add individual Allow groups without copying relevant restrictions: a more specific group overrides the wildcard group. Booking, staging and other excluded pages retain their page-level noindex; they are not promoted through the canonical sitemap.

The optional `llms.txt`, `llms.md` and `.well-known/llms.txt` point to canonical resources, sitemaps, RSS and the extended owner resource index. `llms-full.txt` includes each selected owner resource's title, canonical URL and existing description. Regenerate with `python3 build_discovery_files.py`. These are convenience files, not submission protocols or guaranteed ranking signals. Google explicitly says no special AI file or schema is needed for its AI search features.

Run `python3 audit_ai_access.py` to check all canonical pages against 18 crawler tokens and inspect page directives. Run `python3 audit_ai_access.py --live --output /private/tmp/ae-ai-access.json` to additionally check production content, headers and response codes using ten named user agents across eight core URLs. These are synthetic requests from the operator's machine, not traffic from verified provider IPs. A passing result does not prove crawling, indexing, citations or inclusion in model training.

Search and user retrieval are separate from model training. OAI-SearchBot, Claude-SearchBot, PerplexityBot and MistralAI-Index have search roles; GPTBot and ClaudeBot have different purposes. Google Search AI uses Googlebot. Bing indexing supports Copilot discovery. Keep HTML text, metadata, canonical URLs, internal links and source citations consistent for people and crawlers. Do not serve different claims to bots.

If verified provider traffic is later blocked at the hosting edge, diagnose the actual request and current provider IP documentation before changing a firewall. Never disable the firewall or trust a user-agent string alone. Provider-specific inclusion is only confirmed by that provider's reports, actual retrieval/citations or properly verified crawler logs.

Official references checked September 26, 2026:
- OpenAI: https://developers.openai.com/api/docs/bots
- Anthropic: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Google: https://developers.google.com/search/docs/appearance/ai-features
- Bing: https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a
- Apple: https://support.apple.com/en-gb/119829
- Mistral: https://docs.mistral.ai/robots
