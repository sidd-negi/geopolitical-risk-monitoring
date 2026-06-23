# WEEK 4: STREAMLIT DASHBOARD + VISUALIZATION

import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Geopolitical Risk Monitoring System",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# LOAD DATA (from Week 3 output)
# -----------------------------
df = pd.read_csv("analyzed_news.csv")

# -----------------------------
# TITLE
# -----------------------------
st.title("🌍 Geopolitical Risk Monitoring System")

st.write(
    "This dashboard shows India-related geopolitical news analysis "
    "with sentiment and risk levels."
)

st.divider()

# -----------------------------
# BASIC METRICS
# -----------------------------
total_articles = len(df)

high_risk_df = df[df["risk_level"] == "High"]
high_risk_count = len(high_risk_df)

average_sentiment = df["sentiment_score"].mean()

max_risk_score = df["risk_score"].max()

# Display metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Articles Analyzed", total_articles)

with col2:
    st.metric("High-Risk Articles", high_risk_count)

with col3:
    st.metric("Average Sentiment", round(average_sentiment, 3))

with col4:
    st.metric("Highest Risk Score", max_risk_score)

st.divider()

# -----------------------------
# RISK DISTRIBUTION CHART
# -----------------------------
st.subheader("Risk Level Distribution")

risk_counts = df["risk_level"].value_counts().sort_index()

st.bar_chart(risk_counts)

st.divider()

# -----------------------------
# SENTIMENT TREND
# -----------------------------
st.subheader("Sentiment Trend")

st.line_chart(df["sentiment_score"])

st.divider()

# -----------------------------
# TOP HIGH RISK ARTICLES
# -----------------------------
st.subheader("Top High-Risk Articles")

top_high_risk = df[df["risk_level"] == "High"] \
    .sort_values(by="risk_score", ascending=False)[["title", "risk_score"]].head(20)

st.dataframe(top_high_risk, width="stretch")

st.divider()

# -----------------------------
# SEARCH FUNCTION
# -----------------------------
st.subheader("Search Articles")

keyword = st.text_input("Enter a keyword")

if keyword:
    results = df[df["title"].str.contains(keyword, case=False, na=False)]

    st.write("Total results found:", len(results))

    st.dataframe(
        results[["title", "risk_level", "risk_score"]],
        width="stretch"
    )

st.divider()

# -----------------------------
# DATA PREVIEW
# -----------------------------
with st.expander("View Dataset (First 100 rows)"):

    st.dataframe(df.head(100), width="stretch")