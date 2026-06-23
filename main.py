import pandas as pd
from textblob import TextBlob

# WEEK 1: LOAD DATASET

df = pd.read_csv("india_news.csv")

print("India dataset loaded successfully!")

# WEEK 2: DATA CLEANING

df["text"] = df["text"].fillna("")  
# handle missing values
df = df.drop_duplicates()            
# remove duplicate rows
df["text"] = df["text"].astype(str)  
# ensure text is string

print("Data cleaning completed!")

# WEEK 3: SENTIMENT ANALYSIS

def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

print("Starting sentiment analysis...")

df["sentiment_score"] = df["text"].apply(get_sentiment)

print("Sentiment analysis completed!")

# WEEK 3: RISK SCORE CALCULATION

risk_keywords = [
    "war",
    "conflict",
    "missile",
    "terrorism",
    "sanctions",
    "attack",
    "military",
    "nuclear",
    "violence",
    "border"
]

def calculate_risk(text):
    text = str(text).lower()
    score = 0

    for word in risk_keywords:
        score += text.count(word)

    return score

df["risk_score"] = df["text"].apply(calculate_risk)

# WEEK 3: RISK LEVEL CLASSIFICATION

def risk_level(score):
    if score <= 2:
        return "Low"
    elif score <= 5:
        return "Medium"
    else:
        return "High"

df["risk_level"] = df["risk_score"].apply(risk_level)

# WEEK 3 OUTPUT: SAVE DATASET

df.to_csv("analyzed_news.csv", index=False)

print("Analysis completed successfully!")
# FINAL OUTPUT PREVIEW

print(df.head())