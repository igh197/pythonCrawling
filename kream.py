from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = Options()
user ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

#자동종료 해제
options.add_experimental_option('detach',True)
options.add_argument(f"User-Agent={user}")
#화면크기
#options.add_argument('--start-fullscreen')

#options.add_argument('window-size=500,500')

options.add_argument('--mute-audio')
options.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Chrome(options=options)
#화면X
#options.add_argument('--headless')
url = 'https://www.kream.co.kr'
driver.get(url)
driver.find_element(By.CSS_SELECTOR,'.btn_search').click()
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'.input_search.show_placeholder_on_focus').send_keys('슈프림')
time.sleep(0.3)
driver.find_element(By.CSS_SELECTOR,'.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(0.2)

for i in range(20):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    driver.save_screenshot("/Users/han-ingyu/Desktop/oz_crawling/kream_s/supreme"+str(i)+".png")

html=driver.page_source

soup = BeautifulSoup(html,'html.parser')
items = soup.select(".item_inner")
num=1
for i in items:
    product_name= i.select_one('.translated_name')
    if  '후드' in product_name.text:
        print(num,": ")
        print("상품명: ",i.select_one('.translated_name').text)
        print("브랜드명: ",i.select_one('.product_info_brand.brand').text)
        print("가격: ",i.select_one(".amount").text)
        num+=1
    else:
        continue
    print()

driver.quit()