import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for page in range(1, 6):   # Pages 1 to 5

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        data.append([title, price, rating])

df = pd.DataFrame(
    data,
    columns=["Title", "Price", "Rating"]
)

df.to_csv("books_data.csv", index=False)

print(f"Total Books Collected: {len(df)}")
print("CSV File Saved!")