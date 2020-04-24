# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:43:02 2020

@author: singh
"""
from iexfinance.stocks import Stock
import yfinance as yf
from iexfinance.refdata import get_symbols
import datetime
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np


def main():
    #df = get_symbols(output_format='pandas', token=token)
    df = pd.read_csv("ListOfAllSymbols.csv")
    df = df["symbol"]
    for i in range(len(df)-1):
        x = get_yahoo_data(df[i], period = "6mo", interval = "1d") 
        if len(x) != 0:
            plt.title(df[i])
            x = moving_average(x, 5, 15)
            plt.plot(x["Close"])
            plt.plot(x["SMA"])
            plt.plot(x["LMA"])
            plt.show()
        
def moving_average(x, SMA, LMA):
    x["SMA"] = np.round(x["Close"].rolling(window=SMA, center = False).mean(),2)
    x["LMA"] = np.round(x["Close"].rolling(window=LMA, center = False).mean(),2)
    return x

def get_yahoo_data(ticker, period = "max", interval = "1d"):
    data = yf.download(  # or pdr.get_data_yahoo
        tickers = ticker,

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        period = period,

        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        interval = interval,

        # group by ticker (to access via data['SPY'])
        #group_by = 'ticker',

        # adjust all OHLC automatically
        auto_adjust = True,

        # download pre/post regular market hours data
        #prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        threads = True
    )
    return data
    