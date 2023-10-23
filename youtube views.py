from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.youtube.com/hashtag/%E6%88%91%E7%9A%84%E4%B8%AD%E5%8E%9F%E6%88%91%E7%B4%80%E9%8C%84/shorts"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)

###滑到最下面，讓yt載入更多影片
SCROLL_PAUSE_TIME = 5

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



# headline = driver.find_element(By.ID, 'hashtag').text
# print(headline)

print("開始找!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
videos = driver.find_elements(By.CSS_SELECTOR, 'span.ytd-video-meta-block')
for video in videos:
    print("找到了...")
    print(video.text)
print("找完了，一共找到了",len(videos),"個")
