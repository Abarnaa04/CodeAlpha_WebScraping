import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

# Clean Price column
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)').astype(float)

# 1. Rating Distribution Bar Chart
plt.figure(figsize=(8,5))
df["Rating"].value_counts().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# 2. Price Distribution Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=10)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# 3. Top 10 Expensive Books
top10 = df.nlargest(10, "Price")

plt.figure(figsize=(10,6))
plt.barh(top10["Title"], top10["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")
plt.tight_layout()
plt.savefig("top10_expensive_books.png")
plt.show()

print("Charts created successfully!")