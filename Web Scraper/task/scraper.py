import os

import requests
import string
from bs4 import BeautifulSoup

def get_url() -> str:
   url = input()
   return url


def save_articles(pagenum: int, requested_type: str):
    for num in range(1, pagenum+1):
        url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={str(num)}"
        r = requests.get(url)
        filenames = []
        directory = f"Page_{str(num)}"
        os.mkdir(directory)
        if r:
            soup = BeautifulSoup(r.content, 'html.parser')
            article_type = soup.findAll('span', {'data-test': 'article.type'})
            article_links = []
            for article in article_type:
                # print(article.findNext('span').contents[0])
                if article.findNext('span').contents[0] == requested_type:
                    # print(article.findPrevious('a'))
                    article_links.append(article.findPrevious('a').get('href'))
        else:
            response_status = r.status_code
            print(f"The URL returned {response_status}")
    for link in article_links:
        r = requests.get(f"https://www.nature.com{link}")
        if r:
            soup = BeautifulSoup(r.content, 'html.parser')
            article = soup.findAll('div', 'c-article-body')
            for content in article:
                title = str(content.findPrevious('h1').contents[0])
                # print(title)
                filename = title
                for char in string.punctuation:
                    filename = filename.replace(char, "")
                filename = filename.replace(" ", "_")
                filenames.append(f"{filename}.txt")
                text = ""
                file = open(f"{directory}/{filename}.txt", 'wb')
                file.write(content.getText().encode('utf-8'))
                file.close()
    print(*filenames, sep=" ")
    print("Saved all articles.")

if __name__ == '__main__':
    pages = int(input())
    requested_type = input()
    save_articles(pages, requested_type)





