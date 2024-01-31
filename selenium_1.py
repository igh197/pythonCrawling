from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "https://www.naver.com"

driver=webdriver.Chrome()
driver.get(url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")
query = soup.select_one('#query')
print(query)