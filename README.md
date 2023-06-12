# StockMarketScraper-Extracting-Real-Time-Stock-Data-from-Yahoo-Finance
**Project Aim:**
The primary objective of this project is to extract stock market data from Yahoo Finance for further processing and analysis. The extracted data serves as a valuable resource for various downstream operations, including creating a data pipeline, performing ETL (Extract, Transform, Load) operations, and conducting in-depth analysis. By gathering real-time stock data from different categories, this project lays the foundation for advanced data processing tasks, enabling users to gain insights, make informed investment decisions, and drive strategic business initiatives.

With an aim to gather valuable insights, I am focusing on three intriguing categories: Top Gainer, Top Loser, and Most Active stocks. 
Within each category, I am gathering important details for each stock, including the Symbol and Name, the Price and Price Change, the Volume, as well as the Market Caps.

**Project Components:**
Extraction File: Centralized functions for retrieving stock details.
Top Gainer Stock Python File: Extracts stock details of top gainers.
Top Loser Stock Python File: Extracts stock details of top losers.
Most Active Stock Python File: Extracts stock details of most actively traded stocks.

**Extraction File:**
The "Extraction" file serves as a central repository containing all the necessary functions to retrieve stock details for each category. These functions are responsible for gathering data such as symbols, names, prices, price changes, volumes, and market caps from the specified sources.

**Top Gainer Stock Python File:**
The "Top Gainer Stock" Python file focuses on the category of stocks that are performing exceptionally well. It includes detailed comments for each line of code, enhancing the understanding of the script. This file calls the respective functions from the "Extraction" file to extract and collect the stock details of the top gainers.

Similar to the "Top Gainer Stock" file, the "Top Loser Stock", "Most Active Stock" Python file follows a similar structure.

**Theory**
User Agent: A user agent is a string of information that is sent along with an HTTP request header when a user's browser makes a request to a web server. It identifies the client application, such as a web browser, that is making the request. The user agent string typically includes information about the browser type, version, operating system, and device type. It helps the web server to determine how to handle and render the requested content based on the capabilities and preferences of the client application.

To extract information from this HTML document using Python, you need to parse the HTML structure. Parsing means analyzing the structure and content of the HTML document to identify specific elements and retrieve their data.


Overall, this project is organized into separate Python files, each responsible for extracting stock details from a specific category. The central "Extraction" file contains all the necessary functions, while the other files make use of these functions to extract the desired data.
