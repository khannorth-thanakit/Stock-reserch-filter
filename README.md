# Stock-reserch-filter
Stock Filtering Project
This project leverages Python to efficiently retrieve, analyze, and filter stock data from the SET market. By using a predefined list of stock symbols, the script connects to the yfinance service to fetch essential financial and market data. The core objective is to apply a set of predefined criteria to this data, identifying "interesting" stocks, and then saving the details of these qualifying stocks into an Excel file for easy review and further analysis.

## Main Objectives of the Project:
* **Retrieve Stock Data**: Connect to the yfinance service to fetch financial and market data for each stock.
* **Filter Stocks**: Apply predefined criteria to filter for interesting stocks:
    * **Market Price < 70% of Book Value**: The current market price of the stock must be less than 70% of its book value. This screens for stocks that are trading significantly below their accounting value, potentially indicating an undervalued asset.
    * **EPS > 0**: The Earnings Per Share (EPS) must be greater than zero, meaning the company is currently profitable on a per-share basis. This ensures that the company is generating positive earnings.
    * **Net Income (3 years total) > Total Debt**: The sum of the company's Net Income over the past three years must be greater than its Total Debt. This is a strong indicator of financial health, suggesting the company has generated enough profit to cover its total liabilities, implying good debt management and profitability.
* **Save Results**: Store the data of the filtered stocks into an Excel file for further analysis.

**Technologies Used**: Python, yfinance, pandas, openpyxl

## Disclaimer
#### Please note that this project is intended for informational and analytical purposes only and does not constitute financial advice or a recommendation to buy or sell any securities. Investing in stocks carries inherent risks, and past performance is not indicative of future results. Always conduct your own thorough research and consult with a qualified financial advisor before making any investment decisions.
