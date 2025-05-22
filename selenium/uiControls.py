import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

print(len(checkboxes))

# 리스트를 순회하며 반복할 때마다 하나의 웹 요소를 가져와 변수에 저장
for checkbox in checkboxes:
    # 가져온 변수에서 ID, value, name 속성을 확인 -> get_attribute()
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()      # 해당 체크박스가 선택되었는지 여부 알려주는 메서드
        break


radiobuttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


# is_displayed : 해당 요소가 화면에 표시됐는지 알려줌
assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()


time.sleep(3)
driver.quit()       # selenium이 띄운 모든 브라우저 창 완전히 종료, webdriver 세션도 메모리에서 완전히 정리