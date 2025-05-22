import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = 'yeon'

service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()

# 브라우저 모드에서 경고창 모드로 전환
alert = driver.switch_to.alert
alertText = alert.text      # 경고창에 표시된 텍스트를 가져옴
print(alertText)

assert name in alertText
# ok 버튼 클릭
alert.accept()


time.sleep(3)
driver.quit()  