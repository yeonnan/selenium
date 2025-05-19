import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/client')

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys('hello@world')
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('hello@world')

# driver.find_element(By.XPATH, '//button[@type="submit"]').click()

# xpath는 페이지에 있는 어떤 요소라도 요소의 텍스트를 이용해 요소를 찾을 수 있다.
# //tagname[text()=텍스트]
driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()

time.sleep(5)