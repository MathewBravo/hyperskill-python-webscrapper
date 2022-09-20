import requests
import string
from bs4 import BeautifulSoup

def get_url() -> str:
   url = input()
   return url



if __name__ == '__main__':
    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    r = requests.get(url)
    filenames = []
    print("")
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        article_type = soup.findAll('span', {'data-test': 'article.type'})
        article_links = []
        for article in article_type:
            # print(article.findNext('span').contents[0])
            if article.findNext('span').contents[0] == 'News':
                # print(article.findPrevious('a'))
                article_links.append(article.findPrevious('a').get('href'))
    else:
        response_status = r.status_code
        print(f"The URL returned {response_status}")

    # print(*article_links, sep="\n")
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
                file = open(f"{filename}.txt", 'wb')
                file.write(content.getText().encode('utf-8'))
                file.close()
    # print(*filenames, sep=" ")
    print("Saved articles: " + str(filenames))



