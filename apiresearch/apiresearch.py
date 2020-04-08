from iexfinance.stocks import Stock
import yfinance as yf
token = "pk_5e280dbbce2c454dad7da42f83c4b58f"

#symbol = Stock("AAPL", token = "pk_5e280dbbce2c454dad7da42f83c4b58f")
#symbol.get_company()
#This can be stored too but it is very cheap. API cost = 1

from iexfinance.refdata import get_symbols

df = get_symbols(output_format='pandas', token=token)
#---------------------------------------------------------------------------------------
#df.to_csv(r"PATH/ListOfAllSymbols.csv", index = True)
#list of symbols can be downloaded once and then stored. API cost = 100

stock = Stock("AAPL", token = "pk_5e280dbbce2c454dad7da42f83c4b58f")# creating Stock object. No API cost.

stock_stats = stock.get_key_stats() # only possible with Stock object.
stock_stats
# gets stock info that can be used as stats (in tangent with stocks profile) API cost = 5
"""{'week52change': 0.372464,
 'week52high': 327.85,
 'week52low': 170.27,
 'marketcap': 1148432235600,
 'employees': 137000,
 'day200MovingAvg': 251.36,
 'day50MovingAvg': 285.24,
 'float': 4369507470,
 'avg10Volume': 52168543.5,
 'avg30Volume': 67767145.23,
 'ttmEPS': 12.7549,
 'ttmDividendRate': 3.04,
 'companyName': 'Apple, Inc.',
 'sharesOutstanding': 4375480000,
 'maxChangePercent': 258.8713,
 'year5ChangePercent': 1.061,
 'year2ChangePercent': 0.5588,
 'year1ChangePercent': 0.3117,
 'ytdChangePercent': -0.114,
 'month6ChangePercent': 0.1559,
 'month3ChangePercent': -0.1245,
 'month1ChangePercent': -0.0919,
 'day30ChangePercent': -0.0404,
 'day5ChangePercent': 0.0716,
 'nextDividendDate': None,
 'dividendYield': 0.011582276069646054,
 'nextEarningsDate': '2020-05-05',
 'exDividendDate': '2020-02-07',
 'peRatio': 20.34,
 'beta': 1.1842014268663748}"""

#------------------------------------------------------------------------------------------
# bunch of historical market data. NO api cost
data = yf.download(  # or pdr.get_data_yahoo
        tickers = "MSFT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "5d",

        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True
    )

#-----------------------------------------------------------------------------
stock = Stock("AAPL", token = "pk_5e280dbbce2c454dad7da42f83c4b58f")# creating Stock object. No API cost.
# gets news on stock for example AAPl. API Cost = 10
stock_news = stock.get_news()
print(stock_news)

#--------------------------------------------------------------------------------------------
msft = yf.Ticker("MSFT")

# get stock info. 0 API cost
print(msft.info)


#--------------------------------------------------------------------------------------------
import datetime
import pandas as pd
import pandas_datareader as pdr #pip install pandas_datareader

#loads of data from yahoo finance
def get(tickers, startdate, enddate):
  def data(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
all_data = get(tickers, datetime.datetime(2006, 10, 1), datetime.datetime(2012, 1, 1))
print(all_data)