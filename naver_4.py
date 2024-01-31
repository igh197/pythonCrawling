import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url= input("검색어입력: ")
url = base_url+search_url
req = requests.get(url,headers=header_user)
html = req.text
soup=BeautifulSoup(html,'html.parser')

titles = soup.select(".title_link._cross_trigger")
names= soup.select(".user_info > a") #바로 다음태그 지칭


for i in zip(titles,names):
    print(type(i))
    print(i[0].text)
    print(i[1].text)
    print(i[0]['href'])
    print()