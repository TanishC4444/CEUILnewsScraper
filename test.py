import feedparser
from newspaper import Article
import requests
from urllib.parse import unquote, urlparse, parse_qs

rss_url = "https://www.vox.com/rss/index.xml"

feed = feedparser.parse(rss_url)

for entry in feed.entries[:5]:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")

    # Extract real URL from Google redirect
    parsed_url = urlparse(entry.link)
    if 'url' in parse_qs(parsed_url.query):
        real_url = parse_qs(parsed_url.query)['url'][0]
    else:
        real_url = entry.link

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        html = requests.get(real_url, headers=headers).text
        article = Article(real_url)
        article.set_html(html)
        article.parse()
        print(article.text[:500], "...\n")  # First 500 chars
    except Exception as e:
        print(f"Error fetching article: {e}")

    print("-" * 50)
