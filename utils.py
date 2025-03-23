import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def scrape_news(company_name):
    """Scrape news articles related to the company."""
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey=bb1058cde5c546f78b320810f3c6c9ac"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [{"title": article["title"], "content": article["description"]} for article in data["articles"][:10]]
    return []

def summarize_articles(articles):
    """Generate summaries for the articles."""
    return [article['content'][:150] + "..." if article['content'] else "No summary available" for article in articles]

def analyze_sentiment(summaries):
    """Perform sentiment analysis."""
    sentiments = []
    for summary in summaries:
        polarity = TextBlob(summary).sentiment.polarity
        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")
    return sentiments
