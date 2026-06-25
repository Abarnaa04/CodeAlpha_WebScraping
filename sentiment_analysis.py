import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

reviews = [
    "This book is amazing and very interesting",
    "I love this product",
    "The book is okay",
    "Very disappointing and boring",
    "Worst purchase ever",
    "Excellent quality and great value",
    "Absolutely fantastic experience",
    "Not worth the money",
    "Highly recommended",
    "Average product",
    "Terrible quality",
    "Superb content and presentation",
    "I am very happy with this purchase",
    "Could be better",
    "Outstanding work",
    "Poor packaging",
    "Loved every chapter",
    "Waste of time",
    "Very useful and informative",
    "Decent but not great"
]

df = pd.DataFrame(reviews, columns=["Review"])

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print("\n===== SENTIMENT RESULTS =====")
print(df)

print("\n===== SENTIMENT COUNT =====")
print(df["Sentiment"].value_counts())

# Save results
df.to_csv("sentiment_results.csv", index=False)

# Create chart
sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(6,4))
sentiment_counts.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("sentiment_chart.png")
plt.show()

print("\nSentiment analysis completed!")