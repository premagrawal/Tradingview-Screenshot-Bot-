from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome('/Users/premagrawal/Downloads/chromedriver')
driver.maximize_window()
driver.get('https://www.tradingview.com/#signin')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()
username = ''
password = ''
driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/input').send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.find_element_by_link_text('Chart').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys('NSE:HINDPETRO')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[4]/div/div[1]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header-toolbar-screenshot"]').click()
time.sleep(2)
link = driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[1]/span/input').get_attribute("value")
print(link)
driver.quit()