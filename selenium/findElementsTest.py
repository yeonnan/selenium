import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('kor')
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')
print(len(countries))

for country in countries:
    if country.text == 'Korea, Republic of':
        country.click() 
        break