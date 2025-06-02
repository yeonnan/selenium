import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()


time.sleep(3)
driver.quit()  