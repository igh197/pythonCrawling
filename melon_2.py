from bs4 import BeautifulSoup
from selenium import webdriver
import time

header_user = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://www.melon.com/chart/index.htm"

driver = webdriver.Chrome()
driver.get(base_url)