import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url="https://www.melon.com/chart/index.htm"
req = requests.get(url,headers=header_user)
html = req.text
soup=BeautifulSoup(html,'html.parser')

#tbody50 = soup.select(".lst50")
#tbody100 = soup.select(".lst100")
#tbody = tbody50+tbody100
tbody = soup.find_all(class_=["lst50","lst100"]) 
for rank,body in enumerate(tbody,1):
    print("순위: ",rank)
    title = body.select_one('.ellipsis.rank01 a')
    singer = body.select_one('.ellipsis.rank02 a')
    album = body.select_one('.ellipsis.rank03 a')
    print("제목: "+title.text)
    print("가수: "+singer.text)

    print("앨범: "+album.text)
    print()