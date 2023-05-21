import json
from bs4 import BeautifulSoup
import requests


def get_first_name():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"
    }

    url = "https://www.securitylab.ru/news/"

    query = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(query.text, "lxml")

    articles = []

    article_cards = soup.find_all("a", class_="article-card inline-card")

    for article in article_cards:
        article_title = article.find("h2", class_="article-card-title").get_text()
        article_description = article.find("p").text.strip()
        article_url = f"https://www.securitylab.ru{article.get('href')}"

        articles_data = {
            "title": article_title,
            "description": article_description,
            "url": article_url
        }

        articles.append(articles_data)

        # print(f"{article_title} - {article_description} - {article_url}")

        with open("articles.json", "w") as file:
            json.dump(articles, file, indent=4)

get_first_name()
