import feedparser
from newspaper import Article


# Example RSS feed URL (you can replace this with any valid RSS feed)
rss_url = "https://investor.dallasnewscorp.com/rss/news-releases.xml"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Feed title & info
print(f"Feed Title: {feed.feed.title}")
print(f"Feed Link: {feed.feed.link}")
print(f"Feed Description: {feed.feed.get('subtitle', 'No description')}")

print("\nLatest Entries:\n" + "-" * 50)

# Loop through first 5 articles
for entry in feed.entries[:5]:
    
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.get('published', 'No date')}")
    print(f"Summary: {entry.get('summary', 'No summary')}")
    print("-" * 50)
    article_url = entry.link
    article = Article(article_url)
    article.download()
    article.parse()
    print(article.text)
