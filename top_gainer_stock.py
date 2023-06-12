# Importing the  functions, variables from the 'extract_stock_data' module to retrieve stock data
from extract_stock_data import *

url = 'https://finance.yahoo.com/gainers'
# Send an HTTP request to the URL of the webpage for scraping
top_gainer_list_webpage = requests.get(url, headers = HEADERS)

# Create a BeautifulSoup object to parse the HTML content:
top_gainer_list_soup = BeautifulSoup(top_gainer_list_webpage.content,"html.parser")

# List to store stocks link and stocks symbol 
gainer_stock_link_list = []
gainer_stock_symbol_list = []

# Retrieves the HTML tags or elements where the links and other details to the top gainer stocks reside
top_gainer_stock_link_element = top_gainer_list_soup.find_all("a", attrs = {'class' : "Fw(600) C($linkColor)"})\

# Extracts links, symbols from the retrieved elements and appends them to a list
for details in top_gainer_stock_link_element:
    link = details['href']
    gainer_stock_link_list.append(link)
    gainer_stock_symbol_list.append(details.text)
    
# call the function to retrieve all details of stock in a specific category(i.e, top gainer category)
top_gainer_stock_data_df = get_the_stock_detail(gainer_stock_link_list, gainer_stock_symbol_list)
# save Dataframe into csv file(I'm saving locally, you can upload anywhere: AWS S3 and all by connecting to it)
top_gainer_stock_data_df.to_csv("top_gainer_stock_data.csv", index = False)