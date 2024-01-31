import requests
from bs4 import BeautifulSoup

url="https://www.naver.com"  #naver 주소

req = requests.get(url) #get 요청
#print(req)
html = req.text #req에서 문서부분 기져오기

soup = BeautifulSoup(html,'html.parser') #html을 파싱하기

query = soup.select_one('#query') #아이디 이름인 쿼리로 찾기

print(query) #출력