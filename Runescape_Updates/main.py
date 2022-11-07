import requests
from bs4 import BeautifulSoup

url = "https://secure.runescape.com/m=news/#_ga=2.120857420.556719357.1667805668-523289118.1667805668"
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

# news title
news_title = soup.find_all("a", class_="news-list-article__title-link")
news_date = soup.find_all("time", class_="news-list-article__date")
article = soup.find_all("a", class_="news-list-article__category")

for i in news_title:
    print(i.get_text())

print()
for i in news_date:
    print(i.get_text())

print()
for i in article:
    print(i.get_text())