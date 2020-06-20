import requests
import pandas as pd
import csv
from datetime import datetime as dt

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def strip(df):
    for col in df.columns:
        data = df.pop(col)
        col = col.strip()
        df[col] = data
    return df

# to calculate atm strike
def atm_calculator(n, m):
    a = (n // m) * m
    b = a + m
    return int(b if n - a > b - n else a)

# to get list of symbols in the csv file

def fno_list():
    df = pd.read_csv("https://www1.nseindia.com/content/fo/fo_mktlots.csv")
    df = df.drop(df.index[3])
    fno_list_data = df.iloc[:, 1].to_list()
    fno_list_data = [x.strip(' ') for x in fno_list_data]
    return fno_list_data


# return the required pandas data frame
def Option_Chain_Scrapper(stock_name):
    my_url_nse = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=' + stock_name
    page_nse = requests.get(my_url_nse, headers=header)
    df = pd.read_html(page_nse.text)
    # df[1] is the required table in the page
    return df[1]

# to get future price data (incomplete)


def Future_Price_Scrapper(stock_name):
    my_url_nse = "https://www1.nseindia.com/live_market/dynaContent/live_watch/fomwatchsymbol.jsp?key=" + \
        stock_name + "&Fut_Opt=Futures"
    page_nse = requests.get(my_url_nse, headers=header)
    df = pd.read_html(page_nse.text)
    return df

# to get Lot Size Data
def Lot_Size(stock_name):
    my_url_nse = "https://archives.nseindia.com/content/fo/fo_mktlots.csv"
    df = pd.read_csv(my_url_nse, sep=",")
    df = strip(pd.DataFrame(df))
    month = dt.now().strftime("%b-%y").upper()

    try:
        return float(df.loc[df['SYMBOL'].str.strip() == stock_name][month])
    except:
        return None

# Stocks List from Heatmap
def heatmap_list():
    my_nse_url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/foSecStockWatch.json'
    df = requests.get(my_nse_url,headers=header).json()['data']
    stock_list = []
    for f in df:
        stock_list.append(f['symbol'])
    return stock_list
