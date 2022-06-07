import imp
from sqlite3 import Time
from time import time
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
import time

from utils import get_name_and_pass

options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\web_driver\edgedriver_win64\msedgedriver.exe") # 相应的浏览器的驱动位置
driver.get("https://www.cambly.com/student/login")

# 等待页面加载完成
time.sleep(2)

username, password = get_name_and_pass()

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

# 等待滑块验证
time.sleep(5)
driver.find_element_by_id('login-page-button').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="tutor-search-tabs"]/a[2]').click()
time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, features="html.parser")

soup.find

spans = soup.find_all('span', {'class' : 'tutor-name'})
tutor_names = [span.get_text() for span in spans]


schedule_url_formate = "https://www.cambly.com/en/student/tutors/%s?schedule=&lang=en"

for name in tutor_names:
    name = name.replace(' ', '.') # 将名字中间的空格字符替换为点号字符
    print(schedule_url_formate % name)