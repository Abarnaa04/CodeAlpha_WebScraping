import pandas as pd

# Load dataset
df = pd.read_csv("books_data.csv")

print("===== DATASET OVERVIEW =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== TOTAL BOOKS =====")
print(len(df))

# Convert price to numeric
df["Price"] = df["Price"].str.replace("Â£", "", regex=False).astype(float)
print("\n===== PRICE STATISTICS =====")
print(df["Price"].describe())

print("\n===== MOST EXPENSIVE BOOK =====")
print(df.loc[df["Price"].idxmax()])

print("\n===== CHEAPEST BOOK =====")
print(df.loc[df["Price"].idxmin()])

print("\n===== RATING DISTRIBUTION =====")
print(df["Rating"].value_counts())