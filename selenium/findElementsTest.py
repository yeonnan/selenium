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

'''
.text를 쓸 때 자동화를 통해 스크립트를 동적으로 업데이트하면 텍스트를 못가져온다
-> 웹 애플리케이션 내부에 텍스트가 미리 있어야 가능
=> 변경 사항이 있거나 스크립트를 통해 가져오는 텍스트는 .text로 가져올 수 없다.
'''
# print(driver.find_element(By.ID, 'autosuggest').text)

# 잘 들어왔는지 확인하기
assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'Korea, Republic of'

time.sleep(2)       # 클릭 동작 후, 결과가 반영되는 걸 잠깐 눈으로 볼 수 있게 대기하는 용도
driver.quit()