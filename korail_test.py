from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

pls = 1
start_station = ''
stop_station = ''
start_day = 0
start_month = 0
start_time = 0
min_time = 0

start_station, stop_station = input('출발역과 도착역을 입력하세요: ').split()
start_month = int(input('몇월을 입력하세요: '))
start_day = int(input('몇일을 입력하세요: '))
start_time = int(input('몇시를 입력하세요 (시간은 0 ~ 23): '))
min_time = int(input('몇분을 입력하세요 (0~59): '))
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
e.send_keys(Keys.ENTER)
time.sleep(1)
#e.send_keys(Keys.ENTER)


driver.implicitly_wait(10)
driver.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')


driver.implicitly_wait(3)
e = driver.find_element(By.ID, 'selGoTrainRa00')
e.click()
e = driver.find_element(By.ID, 'start')
e.clear()
e.send_keys(start_station)
e = driver.find_element(By.ID, 'get')
e.clear()
e.send_keys(stop_station)
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
        if ti == 3:
            im = i
            break
                     
    else:
        pass
for j in range(1000):
    driver.implicitly_wait(3)
    if i.get_attribute('alt') == '예약하기':
        i.get_attribute('alt')
        i.click()
        break
    else:
        driver.refresh()
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