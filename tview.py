from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time

csv_path = "/Users/premagrawal/Dropbox/My Mac (Prems-MacBook-Air.local)/Desktop/Entropy/doper.csv"
df = pd.read_csv(csv_path)
del df["Unnamed: 0"]
df["Date"] = pd.to_datetime(df["Date"]).dt.date
df = (df[df['Risk Reward'] > 2 ]).sort_values(by='Risk Reward',ascending=False)
urlList    = []
driver     = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get("https://chrome.google.com/webstore/detail/adblock-%E2%80%94-best-ad-blocker/gighmmpiobklfepjocnamgkkbiglidom")
time.sleep(10)
driver.get('https://www.tradingview.com/#signin')
driver.implicitly_wait(60)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()
username = ''
password = ''
driver.implicitly_wait(60)
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(60)
time.sleep(5)
driver.find_element(By.LINK_TEXT,'Chart').click()
driver.implicitly_wait(60)
time.sleep(5)
for index in range(45,len(df)):
    nextChart = input("Do you want to look at next chart : ")
    if nextChart == "Y" or nextChart == "y":
        print(f"Opening {index}th Chart")
        try:
            driver.find_element(By.CLASS_NAME,"chart-gui-wrapper").click()
            driver.find_element(By.XPATH,'//*[@id="header-toolbar-symbol-search"]').click()
        except:
            driver.find_element(By.XPATH,'//*[@id="header-toolbar-symbol-search"]/div').click()
        driver.implicitly_wait(60)
        stocks = "NSE:" + df.iloc[index]["Stocks"]
        date   = df.iloc[index]["Date"]
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(stocks)
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(60)
        """
        #Close Ad
        try:
            driver.find_element(By.CLASS_NAME,"close-icon-r9bFT7mJ").click()
            driver.implicitly_wait(60)
            try:
                driver.find_element(By.CLASS_NAME,"close-button-aR0iEGbS closeButton-GLTtix84").click()
            except:
                try:
                    driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div[2]/div/div[1]/button').click()
                except:
                    pass
        except:
            pass
        """
        #Jump to Date
        time.sleep(4)
        try:
            driver.find_element(By.CLASS_NAME,'icon-rgQ5VWWu').click()
        except:
            driver.find_element(By.CLASS_NAME,"close-icon-r9bFT7mJ").click()
            time.sleep(1)
            try:
                driver.find_element(By.CLASS_NAME,"close-button-aR0iEGbS closeButton-GLTtix84").click()
            except:
                try:
                    driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div[2]/div/div[1]/button').click()
                except:
                    pass
        driver.implicitly_wait(60)
        element = driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/span/span[1]/input')
        for items in range(10):
            element.send_keys(Keys.BACKSPACE)
        driver.implicitly_wait(60)
        element.send_keys(str(date))
        driver.implicitly_wait(60)
        driver.find_element(By.NAME,"submit").click()
        time.sleep(1)
        #Link-Generate
        driver.find_element(By.XPATH,'//*[@id="header-toolbar-screenshot"]').click()
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[4]/span[2]/span/div/span[2]/span').click()
        time.sleep(3)
        parent = driver.window_handles[0]
        child  = driver.window_handles[1]
        driver.switch_to.window(child)
        url = (driver.current_url)
        if "blob" not in url:
            urlList.append(url)
        else:
            time.sleep(5)
            urlList.append(url)
        driver.close()
        driver.switch_to.window(parent)
