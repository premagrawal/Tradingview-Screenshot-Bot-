from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import requests
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get("https://www.tradingview.com/#signin")
driver.find_element_by_name("username").send_keys("USERNAME")
driver.find_element_by_name("password").send_keys("PASSWORD")
driver.find_element_by_xpath("//button[@type='submit']").click()
try :
    driver.find_element_by_link_text('Chart').click()
except :
    driver.quit()
#driver.find_element_by_class_name('input-3lfOzLDc').clear()
#driver.find_element_by_class_name('input-3lfOzLDc').send_keys('SBIN')
driver.quit()
