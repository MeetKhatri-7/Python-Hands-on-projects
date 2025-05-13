import requests


query=input("What type of news are you interested in today?")
api="2cd4fb9185f84551a7687806bf5a5109"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-04-12&sortBy=publishedAt&apiKey={api}"

print(url)
c=requests.get(url)

data=c.json()
articles =data["articles"]

for index,article in enumerate(articles):
    print(index + 1, article["title"],article["url"])
    print("\n*********************************************\n")