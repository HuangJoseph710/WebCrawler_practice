import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/NBA/index.html"
#在headers中加入User-Agent參數模仿瀏覽器搜尋網站
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("div", class_="r-ent")
for a in articles:
    title = a.find("div", class_="title")
    if title and title.a:
       title = title.a.text
    else:
        title = "沒有標題"

    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"

    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"

    print(f"標題:{title} 人氣{popular} 日期: {date}")
    




'''
if response.status_code == 200:
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("寫入成功!!")
else:
    print("找不到網頁")
'''
