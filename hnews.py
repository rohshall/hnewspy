#!/usr/bin/env python3

from urllib.request import urlopen
import json

response = urlopen("http://hndroidapi.appspot.com/news/format/json/page/")
feed = response.read()
response.close()
articles_map = json.loads(feed.decode("utf-8"))
articles = articles_map["items"]
for article in articles:
  if article.get("item_id"):
    print(article["item_id"] + ": " + article["title"])
    if article.get("url"):
      print(article["url"])
    print()


