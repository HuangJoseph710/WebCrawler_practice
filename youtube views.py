from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

url = "https://www.youtube.com/hashtag/%E6%88%91%E7%9A%84%E4%B8%AD%E5%8E%9F%E6%88%91%E7%B4%80%E9%8C%84/shorts"

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"')
options.add_experimental_option('excludeSwitches', ['enable-automation']) #規避監測
options.add_experimental_option('excludeSwitches', ['enable-logging']) #禁止打印日誌
#options.add_argument('--headless') #無頭模式
options.add_argument('--incognito') #無痕模式

driver = webdriver.Chrome(options=options)

driver.get(url)

try:
    headline = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "hashtag"))
    )
    print(headline.text)
except:
    print("未找到headline!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(5)
    driver.quit()

###滑到最下面，讓yt載入更多影片
SCROLL_PAUSE_TIME = 2

print("開始捲!!!!!!!!!!!!!!")
# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight;")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    print("向下捲了一次!")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight;")
    print(new_height)
    if new_height == last_height:
        if new_height != 4989:
            print("可能出現問題!沒有捲到底!")
        break
    last_height = new_height

#用bs4 找出所有影片的標題(title)和觀看次數(view)
soup = BeautifulSoup(driver.page_source, "html.parser")
contents = soup.find_all("div", id='dismissible')
print("共找到",len(contents),"部影片")

for c in contents:
    title = c.find("span", id='video-title').text
    view = c.find("span", class_='inline-metadata-item style-scope ytd-video-meta-block').text
    print(title)
    print(view)
    print("-"*10)
