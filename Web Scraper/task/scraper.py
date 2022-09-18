import requests
from bs4 import BeautifulSoup

def get_url() -> str:
   url = input()
   return url

if __name__ == '__main__':
    print("Input the URL:")
    url = get_url()
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r:
        if r.status_code > 400:
            print("Invalid movie page!")
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            title = soup.find('h1')
            span = soup.find('span', {'data-testid': 'plot-l'})
            if span is None or title is None:
                print("Invalid movie page!")
            else:
                for child in title.descendants:
                    title_actual = child
                for child in span.descendants:
                    span_actual = child
                title_and_desc = {"title": title_actual, "description": span_actual}
                print(title_and_desc)

    else:
        print("Invalid movie page!")