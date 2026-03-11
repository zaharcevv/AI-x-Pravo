# Legal Radar

AI-powered legal monitoring tool for tracking Slovenian and EU legislative changes.

## What it does

- Scrapes legal portals (e-demokracija, Poročevalec DZ, PISRS, EUR-Lex) for new and upcoming legislative changes
- Uses AI to filter relevant changes and assess their importance
- Classifies changes by legal domain (e.g. energy law, labor law, GDPR)
- Generates concise summaries with key details
- Outputs a structured table: act name, legal domain, publication date, procedure phase, summary, source
- **Bonus:** accepts a short company description and tailors relevant summaries accordingly

## Tech stack

- **Scraping & data:** requests / BeautifulSoup / EUR-Lex API / PISRS API
- **AI layer:** Claude API (filtering, classification, summarization)
- **Output:** structured JSON + human-readable table

## Sources monitored

| Source | Coverage |
|---|---|
| e-demokracija | SI proposals |
| Poročevalec DZ | SI parliamentary procedure |
| PISRS | SI enacted law |
| EUR-Lex | EU legislation |


## Team

Built at [Hackathon Name] 2026.
