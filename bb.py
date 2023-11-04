from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




pls = 1
start_station = ''
stop_staion = ''
start_day = 0
start_month = 0
start_time = 0
min_time = 0
start_station, stop_staion = input('출발역과 도착역을 입력하세요 : ').split()
start_month = int(input('몇월을 입력하세요'))
start_day = int(input('몇일을 입력하세요'))
start_time = int(input('몇시을 입력하세요 (시간은 0 ~ 23)'))
min_time = int(input('몇분을 입력하세요 (0~59)'))
start_day -= 1
start_month -= 1
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
ID = '1063884459'
PW = 'ghdwo!820'
i = 0
url = 'https://www.letskorail.com/korail/com/login.do'
driver.get(url)
driver.implicitly_wait(10)


e = driver.find_element(By.ID, 'txtMember')
e.clear()
e.send_keys(ID)
e = driver.find_element(By.ID, 'txtPwd')
e.clear()
e.send_keys(PW)
e = driver.find_element(By.ID, 'start')
e.clear()
e.send_keys(start_station)
e = driver.find_element(By.ID, 'get')
e.clear()
e.send_keys(stop_staion)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
e = Select(driver.find_element(By.ID, 's_month'))
e.select_by_index(start_month)
e = Select(driver.find_element(By.ID, 's_day'))
e.select_by_index(start_day)
e = Select(driver.find_element(By.ID, 's_hour'))
e.select_by_index(start_time)
e = driver.find_element(By.CLASS_NAME, 'btn_inq')
e.click()


#


main = driver.window_handles
for i in main:
    if i != main[0] :
        driver.switch_to.window(i)
        driver.close()


driver.switch_to.window(main[0])
driver.implicitly_wait(10)


ti = 0
e = driver.find_elements(By.TAG_NAME, 'img')


im = 0


for i in e:
   


    if i.get_attribute('alt') == '예약하기' or i.get_attribute('alt') == '좌석매진' or i.get_attribute('alt') == '입좌석묶음예약':
        ti += 1
        if ti == 5:
            im = i
            break  
    else:
        pass
print(i)
print(im)
for j in range(100):
    im = i
    print(im)
    driver.implicitly_wait(3)
    time.sleep(1)
    if im.get_attribute('alt') == '예약하기':
        im.click()
        break
   
   
    else:
        driver.refresh()
        driver.refresh()
print(im)
       
time.sleep(2)
driver.implicitly_wait(3)


try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
       
        # 취소하기(닫기)
        alert.dismiss()
       
        # 확인하기
        alert.accept()
except:
        pass




driver.implicitly_wait(3)
time.sleep(20)




time.sleep(100)
input()