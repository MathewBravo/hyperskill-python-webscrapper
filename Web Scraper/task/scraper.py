import requests


def get_url() -> str:
   url = input()
   return url

if __name__ == '__main__':
    url = get_url()
    r = requests.get(url)
    if "content" in r.json():
        print(r.json()["content"])
    else:
        print("invalid quote resource!")
