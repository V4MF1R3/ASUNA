import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GNEWS_API_KEY")

if api_key is None:
    raise ValueError("Api key not found. Please set it in the .env file")


def get_news(n=5):
    # returns a sting with multiple headlines.
    url = "https://gnews.io/api/v4/top-headlines"

    params = {
        "lang": "en",
        "country": "in",
        "apikey": api_key,
        "max": n,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "articles" in data:
        articles = data["articles"]
        news = ""
        for article in articles:
            news = news + article["title"] + ".. "
        return news

    else:
        print("No articles found or error:", data)
        return ""


if __name__ == "__main__":
    print(get_news(2))
