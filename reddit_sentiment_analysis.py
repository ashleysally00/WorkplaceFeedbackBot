import pandas as pd
import matplotlib.pyplot as plt

# Load collected data
df = pd.read_csv("reddit_workplace_sentiment.csv")

# Show first few rows
print(df.head())

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Sentiment"], bins=20, edgecolor="black")
plt.xlabel("Sentiment Score")
plt.ylabel("Number of Posts")
plt.title("Sentiment Distribution of Workplace Discussions")
plt.show()

# Show the most positive posts
print("\n🔹 Most Positive Posts:")
print(df.nlargest(3, "Sentiment")[["Title", "Sentiment"]])

# Show the most negative posts
print("\n🔹 Most Negative Posts:")
print(df.nsmallest(3, "Sentiment")[["Title", "Sentiment"]])
