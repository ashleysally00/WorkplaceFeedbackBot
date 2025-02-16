import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables (Make sure you have a .env file)
load_dotenv()

# Get API credentials securely from .env
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Define subreddits to analyze (Professional & Career-Based)
subreddits = ["careerguidance", "jobs", "humanresources", "productivity"]

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Create an empty list to store posts
subreddit_data = []

print("✅ Fetching posts from Reddit...")

# Fetch and analyze posts
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"🔹 Fetching posts from r/{subreddit_name}...")

    for post in subreddit.hot(limit=20):  # Get 20 top posts
        sentiment_score = analyzer.polarity_scores(post.selftext)["compound"]
        subreddit_data.append([subreddit_name, post.title, post.selftext, sentiment_score])

print("✅ Data collection complete. Saving to CSV...")

# Convert to Pandas DataFrame
df = pd.DataFrame(subreddit_data, columns=["Subreddit", "Title", "Body", "Sentiment"])

# Save to CSV
df.to_csv("reddit_workplace_sentiment.csv", index=False)

print("✅ Data saved to reddit_workplace_sentiment.csv!")
