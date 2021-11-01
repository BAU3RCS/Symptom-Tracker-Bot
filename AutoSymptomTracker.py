#Brandon Bauer
#3/10/2020
#Do bs tracker automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = '////////////'
password = '///////////////////' 

driver = webdriver.Firefox()
driver.get('https://portal.lvc.edu/mylvc/login.aspx?ReturnUrl=%2fmylvc%2fapps%2fcovid%2fdailycheck.aspx')
driver.find_element_by_xpath('//*[@id="MainContent_loginControl_UserName"]').send_keys(user)
driver.find_element_by_xpath('//*[@id="MainContent_loginControl_Password"]').send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="MainContent_loginControl_LoginButton"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="WaitingNext"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="NoTemp"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="SymptomsNext"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="ContactNo"]').click()
time.sleep(5)
driver.close()
