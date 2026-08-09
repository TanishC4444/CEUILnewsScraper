# CEUIL News Scraper

A Python news-collection utility that gathers articles for the CEUIL project.

## Requirements

- Python 3.10+
- `feedparser`
- `newspaper3k`
- `lxml`

## Run locally

```bash
python -m pip install feedparser newspaper3k "lxml[html_clean]"
python news_scraper.py
```

Collected articles are written beneath `articles/`.

## Automation

The GitHub Actions workflow can run the scraper on a schedule or manually from the Actions tab.

## Responsible use

Respect source websites' terms of service and rate limits. Treat collected content as working data rather than a permanent source-controlled artifact.
