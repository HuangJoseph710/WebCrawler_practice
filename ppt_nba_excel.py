import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.ptt.cc/bbs/NBA/index.html"
#在headers中加入User-Agent參數模仿瀏覽器搜尋網站
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("div", class_="r-ent")
data_list = []
for a in articles:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
       title = title.a.text
    else:
        title = "沒有標題"
    data["標題"] = title

    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular

    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date

    data_list.append(data)

df = pd.DataFrame(data_list)
df.to_excel("ppt_nba_data.xlsx", index=False, engine="openpyxl")
print("成功匯出成excel檔")