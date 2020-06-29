from Codes import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas
try :
    id = input('Enter your Login ID - ')
    password = input('Enter your Password - ')
    tf = input('Enter chart timeframe  - ')
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    driver.maximize_window()
    driver.get("https://www.tradingview.com/#signin")
    driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div[1]/div[6]/div/div[1]/div/span').click()
    driver.find_element_by_name("username").send_keys(id)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)
    driver.find_element_by_link_text('Chart').click()
    time.sleep(5)
except :
    driver.quit()
#This code changes Timeframe
def change_tf(driver,tf):
    tf_list = ['5m','15m','30m','1H','1D']
    index = str('[' + str(int(tf_list.index(tf)) + 1 ) + ']')
    driver.find_element_by_xpath('//*[@id="header-toolbar-intervals"]/div'+ index).click()
#This function gets called in link_generator if symbol name is changed and generates a URL
def take_screenshot(driver):
    time.sleep(5)
    driver.find_element_by_id("header-toolbar-screenshot").click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"textInput-3WRWEmm7")))
    link = driver.find_element_by_class_name("textInput-3WRWEmm7").get_attribute("value")
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,"close-3kPn4OTV")))
    driver.find_element_by_class_name("close-3kPn4OTV").click()
    return link

#This function clears name of the previous symbols and types new symbol name
def link_generator(driver, stock_name):
    e = driver.find_element_by_class_name('input-3lfOzLDc')
    e.click()
    e.send_keys(Keys.CLEAR)
    e.send_keys(stock_name)
    e.send_keys(Keys.RETURN)
    if e.get_attribute('value') == stock_name:
        links = (take_screenshot(driver))
        return links
try :
    value = heatmap_list()
    url_list = []
    for v in value:
        change_tf(driver,tf)
        link = link_generator(driver,v)
        print(v,'-',link)
        url_list.append(link)
    df = pandas.DataFrame({'Company Name' : value,
                            'Link'        : url_list})
    df.to_csv('sample.csv',header=True)
finally :
    driver.quit()
