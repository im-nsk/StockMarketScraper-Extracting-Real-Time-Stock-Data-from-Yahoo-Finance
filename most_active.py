from extract_stock_data import *

url = "https://finance.yahoo.com/most-active"
most_active_stock_webpage = requests.get(url, headers = HEADERS)
most_active_stock_webpage_parsed = BeautifulSoup(most_active_stock_webpage.content, 'html.parser')

most_active_stock_link_element = most_active_stock_webpage_parsed.find_all('a', class_ = "Fw(600) C($linkColor)")

most_active_stock_link_list = []
most_active_stock_symbol_list = []

for details in most_active_stock_link_element:
    link = details['href']
    most_active_stock_link_list.append(link)
    most_active_stock_symbol_list.append(details.text)

most_active_stock_data_df = get_the_stock_detail(most_active_stock_link_list, most_active_stock_symbol_list)
most_active_stock_data_df.to_csv("most_active_stock_data.csv", index = False)

