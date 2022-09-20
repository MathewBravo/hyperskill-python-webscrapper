import requests
import string
from pathlib import Path
from bs4 import BeautifulSoup

def get_url() -> str:
   url = input()
   return url



if __name__ == '__main__':
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    r = requests.get(url)
    print("")
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        article_type = soup.findAll('article')
        for article in article_type:
            print(article.parents)

    else:
        response_status = r.status_code
        print(f"The URL returned {response_status}")