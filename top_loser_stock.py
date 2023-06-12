from extract_stock_data import *

url = "https://finance.yahoo.com/losers"
top_loser_stock_webpage = requests.get(url, headers = HEADERS)
top_loser_stock_webpage_parsed = BeautifulSoup(top_loser_stock_webpage.content, 'html.parser')

top_loser_stock_list_element = top_loser_stock_webpage_parsed.find_all('a', class_ = "Fw(600) C($linkColor)")

loser_stock_link_list = []
loser_stock_symbol_list = []

for details in top_loser_stock_list_element:
    link = details['href']
    loser_stock_link_list.append(link)
    loser_stock_symbol_list.append(details.text)

top_loser_stock_data_df = get_the_stock_detail(loser_stock_link_list, loser_stock_symbol_list)
top_loser_stock_data_df.to_csv("top_loser_stock_data.csv", index = False)

