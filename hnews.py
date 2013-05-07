#!/usr/bin/env python3

from urllib.request import urlopen
import xml.etree.ElementTree as etree

response = urlopen("https://news.ycombinator.com/rss")
feed = response.read()
response.close()
root = etree.fromstring(feed)
articles = root.find('channel').findall('item')
for article in articles:
    print(article.find("title").text)
    print(article.find("link").text)
    print()
