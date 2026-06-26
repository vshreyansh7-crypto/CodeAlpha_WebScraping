import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# List to store data
books = []

# Find all books
for book in soup.find_all("article", class_="product_pod"):

    # Book Title
    title = book.h3.a["title"]

    # Price
    price = book.find("p", class_="price_color").text

    # Availability
    availability = book.find("p", class_="instock availability").text.strip()

    # Rating
    rating = book.p["class"][1]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

# Convert to DataFrame
df = pd.DataFrame(books)

# Save CSV
df.to_csv("books.csv", index=False)

print(df)

print("\nData Scraped Successfully!")