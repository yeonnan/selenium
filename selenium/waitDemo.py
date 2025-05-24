import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# 태그 이름 속성이 value인 css 사용하는 방법 -> 클래스 이름으로 css 사용 가능
# .클래스_이름
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)       # 검색 후 대기시간

# xpath : //태그명[@속성='값'] -> //div[@class='product-action']
results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(results)
assert count > 0


time.sleep(3)
driver.quit()  