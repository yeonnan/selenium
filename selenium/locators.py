import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('/Users/dayeonahn/Downloads/chromedriver-mac-arm64/chromedriver') 
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')


# Selenium은 ID, XPath, CSS, Classname, name 속성, LinkText 같은 로케이터를 지원
# 로케이터 얻는법 : 브라우저 - 개발자 도구 -> 섹션 찾아서 class 속성

# selenium에게 페이지에 있는 요소 중에 name 로케이터로 입력창을 찾으라고 요청
# 코드를 보고 페이지를 스캔해서 name속성이 login인 요소를 찾게된다.
driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('test1234!')
driver.find_element(By.ID, 'exampleCheck1').click()


'''
name이나 id 같은 것들은 개발자들이 정의해둬야 사용 가능하다.
그런데 어떤 요소, 속성, 정의든 XPath나 CSS는 페이지의 아무 요소에나 활용 가능하다.
'''

# Xpath : //tagname[@attribute='value'] -> //input[@type='submit']
# CSS : tagname[attribute='value'] -> input[type='submit'] / #id속성값 / .classname
driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys('yeon')
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

message = driver.find_element(By.CLASS_NAME, 'alert-success ').text
print(message)      # 어떤 텍스트 값이 취득되든지 message 변수에 저장
assert 'Success' in message     # print 되는 메시지에 Success 라는 키워드가 있는지 확인

driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys('hello')
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()

time.sleep(5)