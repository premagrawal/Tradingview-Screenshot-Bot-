from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import requests
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.implicitly_wait(60)
driver.get("https://www.tradingview.com/#signin")
driver.find_element_by_name("username").send_keys("username")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_link_text('Chart').click()
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/input').send_keys('SBIN')
driver.quit()
