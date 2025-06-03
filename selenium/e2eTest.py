import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()
products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for product in products:
    productName = product.find_element(By.XPATH, 'div/h4/a').text
    if productName == 'Blackberry':
        product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()

time.sleep(3)
driver.quit()  