import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url= input("검색어입력: ")
url = base_url+search_url
req = requests.get(url,headers=header_user)
html = req.text
soup=BeautifulSoup(html,'html.parser')

areas=soup.select(".view_wrap")

for i in areas:
    ad = i.select_one(".link_ad")
    if ad :
        continue
    else:
        title = i.select_one(".title_link._cross_trigger")
        name= i.select_one(".user_info > a") 
        print("글제목: "+ title.text)
        print("블로그 작성자: "+name.text)
        print("글링크: "+title['href'])
        print()