import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('kor')
time.sleep(2)       # 자동완성 드롭다운이 뜰 때까지 기다리는 용도
countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')
print(len(countries))

for country in countries:
    if country.text == 'Korea, Republic of':
        country.click() 
        break

time.sleep(2)       # 클릭 동작 후, 결과가 반영되는 걸 잠깐 눈으로 볼 수 있게 대기하는 용도
driver.quit()