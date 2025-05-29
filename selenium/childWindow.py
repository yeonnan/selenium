import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT, 'Click Here').click()
windowsOpened = driver.window_handles       # 열려있는 모든 창의 이름을 가져오는 프로퍼티

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()

driver.switch_to.window(windowsOpened[0])
assert 'Opening a new window' == driver.find_element(By.TAG_NAME, 'h3').text 

time.sleep(3)
driver.quit()  