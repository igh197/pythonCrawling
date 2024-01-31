from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = Options()
user ="Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36"
#자동종료 해제
options.add_experimental_option('detach',True)
options.add_argument(f"user-agent={user}")
#화면크기
#options.add_argument('--start-fullscreen')

#options.add_argument('window-size=500,500')

options.add_argument('--mute-audio')
options.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Chrome(options=options)
#화면X
#options.add_argument('--headless')
url = 'https://m2.melon.com/index.htm'
driver.get(url)
time.sleep(3)
if url!=driver.current_url:
    driver.get(url)
time.sleep(1)
driver.find_element(By.LINK_TEXT,"닫기").click()
time.sleep(0.2)
driver.find_element(By.LINK_TEXT,"멜론차트").click()
time.sleep(0.2)
more_btn = driver.find_elements(By.CSS_SELECTOR,'#moreBtn')
more_btn[1].click()

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find_all(class_="list_item") 
for rank,body in enumerate(tbody,1):
    print("순위: ",rank)
    title = body.select_one('.title.ellipsis')
    singer = body.select_one('.name.ellipsis')
    print("제목:",end="")
    print(title.text.strip())
    print("가수: ",end="")
    print(singer.text)
    print()

