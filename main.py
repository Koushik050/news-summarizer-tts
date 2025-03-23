import streamlit as st
import requests
from utils import scrape_news, analyze_sentiment, summarize_articles
from tts import text_to_speech

st.title("News Summarization & TTS")

company_name = st.text_input("Enter Company Name")

if st.button("Fetch News") and company_name:
    articles = scrape_news(company_name)
    if not articles:
        st.error("No articles found.")
    else:
        summaries = summarize_articles(articles)
        sentiments = analyze_sentiment(summaries)

        st.subheader("News Analysis")
        for i, article in enumerate(articles):
            st.write(f"### {article['title']}")
            st.write(f"Summary: {summaries[i]}")
            st.write(f"Sentiment: {sentiments[i]}")

        final_summary = " ".join(summaries)
        st.subheader("Hindi Speech Output")
        audio_path = text_to_speech(final_summary)
        st.audio(audio_path, format='audio/mp3')
