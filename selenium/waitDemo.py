import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

# 암시적 대기 : 스크립트 가장 위에서 한번만 선언하면 모든 요소를 찾을 때마다 최대 지정한 시간만큼 기다려준다.
driver.implicitly_wait(5)

# 페이지에 아무 요소도 뜨지 않으면 뜰 때까지 최대 5초 대기. 찾을때까지 맹목적으로 대기하는게 아닌 최대 대기시간
# sleep으로 대기하는 경우는 무조건 해당 시간을 다 기다리는데, 암시적 대기는 전반적인 대기시간을 설정하고, 그 안에 요소가 표시되면 다음 단계를 진행

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# 태그 이름 속성이 value인 css 사용하는 방법 -> 클래스 이름으로 css 사용 가능
# .클래스_이름
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)       # 검색 후 대기시간

# xpath : //태그명[@속성='값'] -> //div[@class='product-action']
results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)


time.sleep(3)
driver.quit()  