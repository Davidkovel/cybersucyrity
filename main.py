from bs4 import BeautifulSoup
import requests


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"
    }

    url = "https://www.securitylab.ru/news/"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    article_cards = soup.find_all("a", class_="article-card inline-card")

    for article in article_cards:
        article_title = article.find('h2', class_="article-card-title").get_text()
        article_desc = article.find("p").text.strip()
        article_url = f"https://www.securitylab.ru{article.get('href')}"

        print(f"{article_title} | {article_desc} | {article_url}")


get_first_news()
