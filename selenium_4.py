from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
url = 'https://www.naver.com'
driver.get(url)