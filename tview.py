from Codes import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv
from collections import defaultdict
try :
    id = input('Enter your Login ID - ')
    password = input('Enter your Password - ')
    tf = input('Enter chart timeframe  - ')
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    driver.maximize_window()
    driver.get("https://www.tradingview.com/#signin")
    driver.find_element_by_name("username").send_keys(id)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)
    driver.find_element_by_link_text('Chart').click()
    time.sleep(5)
except :
    driver.quit()
def take_screenshot(driver):
    e = driver.find_element_by_id("header-toolbar-screenshot")
    e.click()
    time.sleep(2)
    e = driver.find_element_by_class_name("textInput-3WRWEmm7")
    link = e.get_attribute("value")
    time.sleep(1)
    e = driver.find_element_by_class_name("close-3kPn4OTV")
    e.click()
    time.sleep(2)
    return link
def change_tf(driver,tf):
    tf_list = ['5m','15m','30m','1H','1D']
    # 5m //*[@id="header-toolbar-intervals"]/div[1]
    # 15m //*[@id="header-toolbar-intervals"]/div[2]
    # 30m //*[@id="header-toolbar-intervals"]/div[3]
    # 1H //*[@id="header-toolbar-intervals"]/div[4]
    # 1D //*[@id="header-toolbar-intervals"]/div[5]
    index = str('[' + str(int(tf_list.index(tf)) + 1 ) + ']')
    driver.find_element_by_xpath('//*[@id="header-toolbar-intervals"]/div'+ index).click()
def link_generator(driver, stock_name):
    e = driver.find_element_by_class_name('input-3lfOzLDc')
    e.click()
    time.sleep(1)
    e.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    e.send_keys(stock_name)
    time.sleep(1)
    e.send_keys(Keys.RETURN)
    time.sleep(3)
    links = (take_screenshot(driver))
    return links
try :
    value = heatmap_list()
    res = defaultdict(list)
    for v in value:
        change_tf(driver,tf)
        link = link_generator(driver,v)
        print(v,link)
        res[v].append(link)
        time.sleep(2)
        row_list = ["STOCK SYMBOL","LINK"]
    for k in res.keys():
        row = [k]
        row += res[k]
        row_list.append(row)
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(row_list)
finally :
    driver.quit()
