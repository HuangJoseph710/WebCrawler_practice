import requests
from bs4 import BeautifulSoup
import os

url="https://www.ptt.cc/bbs/Beauty/M.1696008245.A.892.html"

headers = {"Cookie": "over18=1"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

spans = soup.find_all("span", class_="article-meta-value")
title = spans[2].text
dir_name = f"images/{title}"
os.makedirs(dir_name)
