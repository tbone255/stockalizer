# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:57:57 2020

@author: Ash
"""
from iexfinance.refdata import get_symbols
import os
from twitter.models import Ticker, Trend, News, NewsTrend, PriceInfo
from django.core.management.base import BaseCommand, CommandError
import yfinance as yf
from TwitterSearch import *
from datetime import date, timedelta
from datetime import datetime
from iexfinance.stocks import Stock
import time


class Command(BaseCommand):
    help = 'create the trends for each ticker'

    def __init__(self):
        self.iex_token = os.getenv('IEX_TOKEN')
        self.t_access_token = os.getenv('T_ACCESS_TOKEN')
        self.t_access_token_secret = os.getenv('T_ACCESS_TOKEN_SECRET')
        self.t_consumer_key = os.getenv('T_CONSUMER_KEY')
        self.t_consumer_secret = os.getenv('T_CONSUMER_SECRET')

    def get_logo(self,symbol):
        symbol = Stock(symbol, token=self.iex_token)
        return symbol.get_logo() #return dict / df of url to the logo of company
    
    def get_stock_stats(self, symbol):
        symbol = Stock(symbol, token=self.iex_token)
        """
        {'week52change': 0.372464,'week52high': 327.85,'week52low': 170.27,
         'marketcap': 1148432235600,'employees': 137000,'day200MovingAvg': 251.36,
         'day50MovingAvg': 285.24,'float': 4369507470,'avg10Volume': 52168543.5,
         'avg30Volume': 67767145.23,'ttmEPS': 12.7549,'ttmDividendRate': 3.04,
         'companyName': 'Apple, Inc.','sharesOutstanding': 4375480000,'maxChangePercent': 258.8713,
         'year5ChangePercent': 1.061,'year2ChangePercent': 0.5588,'year1ChangePercent': 0.3117,
         'ytdChangePercent': -0.114, 'month6ChangePercent': 0.1559,'month3ChangePercent': -0.1245,
         'month1ChangePercent': -0.0919,'day30ChangePercent': -0.0404,'day5ChangePercent': 0.0716,
         'nextDividendDate': None,'dividendYield': 0.011582276069646054,'nextEarningsDate': '2020-05-05',
         'exDividendDate': '2020-02-07','peRatio': 20.34,'beta': 1.1842014268663748}
        """
        return stock.get_key_stats() # only possible with Stock object.

    def get_stock_info(self, symbol):
        symbol = Stock(symbol, token=self.iex_token)
        """ THIS IS WHAT THE OUTPUT LOOKS LIKE
        {'symbol': 'AAPL', 'companyName': 'Apple, Inc.', 'exchange': 'NASDAQ', 
         'industry': 'Telecommunications Equipment', 'website': 'http://www.apple.com', 
         'description': 'Apple, Inc. engages in the design, manufacture, and sale of smartphones, 
         personal computers, tablets, wearables and accessories, and other variety of related services. 
         It operates through the following geographical segments: Americas, Europe, Greater China, 
         Japan, and Rest of Asia Pacific. The Americas segment includes North and South America.
         The Europe segment consists of European countries, as well as India, the Middle East, 
         and Africa. The Greater China segment comprises of China, Hong Kong, and Taiwan. 
         The Rest of Asia Pacific segment includes Australia and Asian countries. Its products 
         and services include iPhone, Mac, iPad, AirPods, Apple TV, Apple Watch, Beats products,
         Apple Care, iCloud, digital content stores, streaming, and licensing services. The company 
         was founded by Steven Paul Jobs, Ronald Gerald Wayne, and Stephen G. Wozniak on 
         April 1, 1976 and is headquartered in Cupertino, CA.', 'CEO': 'Timothy Donald Cook', 
         'securityName': 'Apple Inc.', 'issueType': 'cs', 'sector': 'Electronic Technology', 
         'primarySicCode': 3663, 'employees': 137000, 'tags': ['Electronic Technology', 
         'Telecommunications Equipment'], 'address': 'One Apple Park Way', 'address2': None, 
         'state': 'CA', 'city': 'Cupertino', 'zip': '95014-2083', 'country': 'US', 
         'phone': '1.408.996.1010'}
        """
        return symbol.get_company()
    def get_news(self, symbol):
        stock = Stock(symbol, token=self.iex_token)# creating Stock object. No API cost.
        # gets news on stock for example AAPl. API Cost = 10
        return stock.get_news()    
    
    def handle(self, *args, **options):
        # Don't know how to rate limit 
        x = date.today()
        y =  x - timedelta(days=1)
        
        #CODE REUSE FROM TwitterSearchAPI +minor changes to layout
        tso = TwitterSearchOrder()
        tso.set_language('en') 
        tso.set_since(y)
        tso.set_until(x)
        ts = TwitterSearch(consumer_key= self.t_consumer_key, consumer_secret = self.t_consumer_secret,
                        access_token = self.t_access_token, access_token_secret = self.t_access_token_secret)
        for e in Ticker.objects.all():           
            priceinfo_obj = PriceInfo.objects.create(yesterclose = 0, first_mention = 0, last_price = 0, last_volume = 0)
            symbol = "$"+ e.symbol
            #numoftweets = self.get_number_of_tweets(symbol)
            tweets = []
            result = 0             
            try:
               tso.set_keywords([symbol]) 
               def my_callback_closure(ts): 
                   queries, tweets_seen = ts.get_statistics()      
                   if queries > 0 and (queries % 13) == 0: # DONT CHANGE QUERY IT IS CUSTOMIZED
                       print("Sleeping to prevent rate limit.")
                       time.sleep(70) # DONT CHANGE SLEEP TIME IT IS CUSTOMIZED
                
               df = ts.search_tweets_iterable(tso, callback = my_callback_closure)
            
               for tweet in df:
                   tweets.append(tweet)       
                
               result = len(tweets) 
                      
            except TwitterSearchException as e:         
                result = -1
                print(e)
                
           
            numoftweets = result
            if numoftweets == -1:
                print("Error occured. Sleeping for 15 minutes.")
                time.sleep(900)
            news = self.get_news(e.symbol)
                
            trend_obj = Trend.objects.create(ticker_id = e, count = numoftweets,
                                                 priceinfo_id = priceinfo_obj)
            for article in news:
                if len(article['url']) > 200 or len(article['headline']) > 200:
                    continue
                new_object = News.objects.create(url = article["url"], title = article["headline"] )
                newtrade_obj = NewsTrend.objects.create(trends_id = trend_obj, news_id = new_object)
            print("Stock: "+e.symbol+" #Tweets: "+str(numoftweets)+" #news: "+str(len(news)))


   
    
    
                
        
