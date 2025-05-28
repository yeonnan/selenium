import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)       # 검색 후 대기시간


results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(results)
assert count > 0

for result in results:
    actualList.append(result.find_element(By.XPATH, 'h4').text)
    result.find_element(By.XPATH, 'div/button').click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()

# 총액 검증
prices = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)

discounteAmount = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)
assert totalAmount > discounteAmount

time.sleep(3)
driver.quit()  