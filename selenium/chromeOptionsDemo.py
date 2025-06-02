import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore-certificate-errors')

service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)

time.sleep(3)
driver.quit()  