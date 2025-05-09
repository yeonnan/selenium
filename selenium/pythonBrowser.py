from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

# 크롬 브라우저에서 url 열기
driver.get('https://github.com/yeonnam')
print(driver.title)     # 페이지 제목
print(driver.current_url)      # 현재 url 조회
driver.close()