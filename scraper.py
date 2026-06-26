import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store extracted data
quotes = []

# Extract quote and author
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quotes.append({
        "Quote": text,
        "Author": author
    })

# Convert to DataFrame
df = pd.DataFrame(quotes)

# Save dataset
df.to_csv("data.csv", index=False)

print("Data Scraped Successfully!")
print(df)