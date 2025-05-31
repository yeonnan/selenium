import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame('mce_0_ifr')

# 파이어폭스는 clear() 지원하지만, 크롬은 input/textarea에서만 clear() 동작함
# tinymce는 <body>라 크롬에서 clear() 사용 불가
# driver.find_element(By.ID, 'tinymce').clear()
# driver.find_element(By.ID, 'tinymce').send_keys('힝입니다.')

driver.find_element(By.ID, 'tinymce').send_keys(Keys.CONTROL, 'a')
driver.find_element(By.ID, 'tinymce').send_keys(Keys.DELETE)
driver.find_element(By.ID, 'tinymce').send_keys('힝입니다.')

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)

time.sleep(3)
driver.quit()  