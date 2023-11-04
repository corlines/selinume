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

srt_month = 0
srt_day = 0
srt_time = 0
srt_start_station = ''
srt_end_station = ''
srt_start_station,srt_end_station = input('출발역과 도착역을 입력하세요 : ').split()
srt_month= int(input('몇월을 입력하세요:'))
srt_day = int(input('몇일을 입력하세요'))
srt_time = int(input('시간을 입력하세요 (0~22 짝수만) : '))
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                       options=chrome_options)
id = ''
pw = ''
url = 'https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000'
driver.get(url)
driver.implicitly_wait(10)

e = driver.find_element(By.ID, 'srchDvNm01')
e.send_keys(id)
e = driver.find_element(By.ID ,'hmpgPwdCphd01')
e.send_keys(pw)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000')
e = driver.find_element(By.ID ,'dptRsStnCdNm')
e.send_keys(srt_start_station)
e = driver.find_element(By.ID, 'arvRsStnCdNm')
e.send_keys(srt_end_station)
e = Select(driver.find_element(By.ID, 'dptDt'))
e.select_by_index(srt_month)