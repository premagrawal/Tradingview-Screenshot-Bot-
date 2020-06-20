from Codes import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv
from collections import defaultdict

id = input('Enter your Login ID - ')
password = input('Enter your Password - ')
tfs = input("Enter TFs in minutes separated by comma : ")
tfs = map(int, tfs.split(','))

#TF = input('Enter Timeframe (15,30,60,1440) - ')
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.implicitly_wait(30)
driver.get("https://www.tradingview.com/#signin")
driver.find_element_by_name("username").send_keys(id)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.find_element_by_link_text('Chart').click()
time.sleep(7)
def take_screenshot(driver):
    e = driver.find_element_by_id("header-toolbar-screenshot")
    e.click()
    time.sleep(5)
    e = driver.find_element_by_class_name("textInput-3WRWEmm7")
    link = e.get_attribute("value")
    time.sleep(1)
    e = driver.find_element_by_class_name("close-3kPn4OTV")
    e.click()
    time.sleep(2)
    return link
def change_tf(driver, tf_in_min):
    e = driver.find_element_by_xpath("/html/body")
    e.send_keys(str(tf_in_min))
    time.sleep(1)
    e.send_keys(Keys.RETURN)
    time.sleep(5)
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

value = heatmap_list()
res = defaultdict(list)
for x in tfs:
    change_tf(driver, x)
    change_tf(driver, x)
    change_tf(driver, x)
    for v in value:
        print(v)
        link = link_generator(driver,v)
        res[v].append(link)
        time.sleep(5)
row_list = []
for k in res.keys():
    row = [k]
    row += res[k]
    row_list.append(row)
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(row_list)
