import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# 헤드 모드로 실행하면 브라우저가 열리고 모든 작업을 볼 수 있다.
# 헤드리스 모드로 실행하면 브라우저가 열리는 것을 볼 수 없다.

# 헤드리스 모드 - 크롬 옵션 선언 필요
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

chrome_options.add_argument('--ignore-certificate-errors')      # 모든 인증 오류 무시

service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

'''
크롬 화면에서 스크롤 내리는 작업 : 콘솔 - windo.scrollTo(0, 500) <- 여기서 500은 높이
제일 하단으로 내리기 window.scrollTo(0, document.body.scrollHeight)
'''
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')     # 자바스크립트 작업 실행
driver.get_screenshot_as_file('screen.png')     # 스크린샷 촬영

time.sleep(3)
driver.quit()  