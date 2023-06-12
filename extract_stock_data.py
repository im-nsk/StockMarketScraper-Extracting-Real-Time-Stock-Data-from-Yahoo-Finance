import requests
from bs4 import BeautifulSoup
import pandas as pd

# User agent
HEADERS = ({'User-agent' : '*****KEEP YOUR USER AGENT*****', 'Accept-Language' : 'en-US, en; q=0.5'})

#  Create all required list
stocks_name = []
stocks_price = []
stocks_price_change = []
stocks_percent_change = []
stocks_volume = []
stocks_market_cap = []
stock_data = []

def get_the_stock_detail(stock_link_list, stock_symbol_list):
    
    for link in stock_link_list:
        url = 'https://finance.yahoo.com' + link
        stock_webpage = requests.get(url, headers = HEADERS)
        stock_webpage_parsed = BeautifulSoup(stock_webpage.content, 'html.parser')

        # get all detail by function
        stocks_name.append(get_the_stock_name(stock_webpage_parsed))
        stocks_price.append(get_the_stock_price(stock_webpage_parsed))
        stocks_price_change.append(get_the_stock_price_change(stock_webpage_parsed))
        stocks_percent_change.append(get_the_stock_percent_change(stock_webpage_parsed))
        stocks_volume.append(get_the_stock_volume(stock_webpage_parsed))
        stocks_market_cap.append(get_the_stock_market_cap(stock_webpage_parsed))
        
    num_of_stocks = len(stock_link_list)
    for i in range(num_of_stocks):
        stock_data_mapping = {
                "stocks_Symbol" : stock_symbol_list[i],
                "stocks_name" : stocks_name[i],
                "stocks_price" : stocks_price[i],
                "stocks_price_change" : stocks_price_change[i],
                "stocks_percent_change" : stocks_percent_change[i],
                "stocks_volume" : stocks_volume[i],
                "stocks_market_cap" : stocks_market_cap[i]
            }
        # append the mapped data
        stock_data.append(stock_data_mapping)


    # Create a dataFrame
    return pd.DataFrame(stock_data)


# Detail 1: stock_name
def get_the_stock_name(stock_webpage_parsed):
    stock_detail = stock_webpage_parsed.find('h1', class_="D(ib) Fz(18px)")
    result = stock_detail.text
    return result

# Detail 2: stock_price
def get_the_stock_price(stock_webpage_parsed):
    stock_detail = stock_webpage_parsed.find(class_ ="Fw(b) Fz(36px) Mb(-4px) D(ib)")
    result = stock_detail['value']
    return result

# Detail 3: stock_price_change
def get_the_stock_price_change(stock_webpage_parsed):
    stock_detail = stock_webpage_parsed.find('div', class_ = "D(ib) Mend(20px)").find_all('span')
    result = stock_detail[0].text
    return result

# Detail 4: stock_price_change_in_percent
def get_the_stock_percent_change(stock_webpage_parsed):
    stock_detail = stock_webpage_parsed.find('div', class_ = "D(ib) Mend(20px)").find_all('span')
    result = stock_detail[1].text
    return result

# Detail 5: stock_Volume
def get_the_stock_volume(stock_webpage_parsed):
    stock_detail =  stock_webpage_parsed.find("td", class_ = "Ta(end) Fw(600) Lh(14px)", attrs = {"data-test": "TD_VOLUME-value"})
    result = stock_detail.text
    return result

# Detail 6: stock_mark_cap
def get_the_stock_market_cap(stock_webpage_parsed):
    stock_detail = stock_webpage_parsed.find("td", class_ = "Ta(end) Fw(600) Lh(14px)", attrs = {"data-test": "MARKET_CAP-value"})
    result = stock_detail.text
    return result

