from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 크롬 브라우저에서 테스트 할 수 있게 해주는 역할
service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)


driver.maximize_window()        # 전체화면
# 크롬 브라우저에서 url 열기
driver.get('https://github.com/yeonnan')
print(driver.title)     # 페이지 제목
print(driver.current_url)      # 현재 url 조회
driver.get('https://github.com/yeonnan/OneDayChat')
driver.minimize_window()     # 창 최소화 하기
driver.back()     # 이전 페이지로 돌아가기
driver.refresh()        # 페이지 새로고침
driver.forward()        # 앞으로 가기
driver.close()

# 제목이랑 현재 url을 출력하고 웹사이트로 이동하고 브라우저는 닫힘