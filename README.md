# CEUIL News Scraper

A Python utility that collects news articles for the CEUIL project and stores the collected material for downstream processing.

## Overview

The scraper retrieves articles from configured news sources and writes collected content beneath `articles/`. GitHub Actions can run the workflow on a schedule or on demand.

## Features

- Automated article collection
- Feed and article parsing
- Local article storage
- Scheduled GitHub Actions execution
- Manual workflow execution
- Responsible-use guidance for third-party sources

## Prerequisites

- Python 3.10+
- pip

## Installation

```bash
git clone https://github.com/TanishC4444/CEUILnewsScraper.git
cd CEUILnewsScraper
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install feedparser newspaper3k "lxml[html_clean]"
```

## Quick Start

```bash
python news_scraper.py
```

Collected articles are written beneath `articles/`.

## Automation

GitHub Actions can execute the scraper on a schedule or through a manual workflow dispatch.

## Responsible Use

Respect source websites' terms of service, robots policies where applicable, and rate limits. Treat collected content as working data rather than a permanent source-controlled archive.

## License

No separate license is currently specified in the repository.

## Support

Use GitHub Issues for bugs and project questions.
