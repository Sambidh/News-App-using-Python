import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-02&sortBy=publishedAt&apiKey=760579cd025945baa143f7634ef0a9c3"

r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------")
