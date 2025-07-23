import feedparser
from newspaper import Article
from time import sleep
from datetime import datetime
import os
import re

# --- CONFIG ---
FEEDS = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "NPR": "https://feeds.npr.org/1001/rss.xml",
    "CNN": "http://rss.cnn.com/rss/cnn_topstories.rss",
    "PBS NewsHour": "https://www.pbs.org/newshour/feeds/rss/headlines",
    "Washington Post": "https://feeds.washingtonpost.com/rss/national",
    "NY Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
}
MAX_ARTICLES = 100
WAIT_BETWEEN = 0.02
OUTPUT_DIR = "savedarticles"
CHUNK_LIMIT = 36000
# --- Setup Output File ---
timestamp = datetime.now().strftime("%Y-%m-%d%H-%M")
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_path = os.path.join(OUTPUT_DIR, f"articles.txt")
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write(f"\n==== 🕒 Run at {datetime.now().isoformat()} ====\n")
    char_written = 0
    for name, url in FEEDS.items():
        print(f"\n====== 📰 {name} ======")
        #out_file.write(f"\n====== 📰 {name} ======\n")
        feed = feedparser.parse(url)
        entries = feed.entries[:MAX_ARTICLES]
        for i, entry in enumerate(entries, 1):
            article_url = entry.link
            title = entry.title.strip()
            try:
                article = Article(article_url)
                article.download()
                article.parse()
                text = article.text.strip()
                # Fallback: use RSS summary if text is too short
                if not text or len(text) < 100:
                    text = entry.get("summary", "").strip()
                    if not text:
                        raise ValueError("No article text or summary found.")
                print(f"\n{i}. {title}")
                #print(f"🔗 {article_url}")
                #print(f"📰 {text[:200]}...")
                # Save to file
                #out_file.write(f"\n{i}. {title}\n")
                out_file.write(f"{article_url}\n")
                text = re.sub(r'\b[a-z]{1,3}\b', '', text)
                char_written += len(text)
                if char_written >= CHUNK_LIMIT:
                    out_file.write("\n" + "-"*50 + "\n")
                    char_written = 0
                out_file.write(f"{text}\n")
                out_file.write("\n" + "-"*5 + "\n")
            except Exception as e:
                print(f"\n{i}. ❌ Failed: {title}")
                #print(f"🔗 {article_url}")
                print(f"Error: {e}")
                #out_file.write(f"\n{i}. ❌ Failed: {title}\n🔗 {article_url}\nError: {e}\n")
            sleep(WAIT_BETWEEN)
print(f"\n✅ Articles saved to: {output_path}")