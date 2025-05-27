import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

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

# 명시적 대기 : 하나의 특정 요소를 지정해서 그 요소에만 독점적으로 최대 대기 시간 설정가능
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)

time.sleep(3)
driver.quit()  


'''
암시적 대기는 애플리케이션이 페이지를 로드하는 데 걸릴 수 있는 기본 대기시간을 전체적으로 적용
명시적 대기는 예외적으로 로딩에 시간이 조금 더 걸리는 요소를 대상으로 사용
''' 