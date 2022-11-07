import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

quote = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

print()
for i in range(len(quote)):
    print("1.", author[i].get_text(), "\n", quote[i].get_text())
    print()

print()
