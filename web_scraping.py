import requests
from bs4 import BeautifulSoup

ur1 = "https://quotes.toscrape.com"

response = requests.get(ur1)
soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("span",class_="text")
authors = soup.find_all("small",class_="author")

print("Quotes and authors\n")
for quote, author in zip(quotes,authors):
 print(f"Quote: {quote.text}")
print(f"Author: {author.text}")
print("_" * 40)
