
from bs4 import BeautifulSoup
from selenium import webdriver
import time

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url= input("검색어입력: ")
url = base_url+search_url

driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)

#스코롤 코드
#driver.execute_script("window.scrollTo(0,4000)")
#time.sleep(2)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#time.sleep(5)

for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    areas = soup.select('.view_wrap')
    num = 1
    for i in areas:
        ad = i.select_one('.link_ad')
        if ad :
            continue
        else:
            title = i.select_one(".title_link._cross_trigger")
            name= i.select_one(".user_info > a") 
            print("글제목: "+ title.text)
            print("블로그 작성자: "+name.text)
            print("글링크: "+title['href'])
            print()
