# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:32:19 2020

@author: Ash
"""
import os
from iexfinance.refdata import get_symbols
from twitter.models import Ticker
from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
import pandas as pd

class Command(BaseCommand):
    help = 'create the tickers in the database'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_ids', nargs='+', type=int)

    
        
    def handle(self, *args, **options):
        token = os.getenv('IEX_TOKEN')
        df = get_symbols(token = token)   

        ticker_id = 1
        start_at_id = 124

        for i in range(len(df)):
            if ticker_id < start_at_id:
                ticker_id += 1
                continue
            
            print("Symbol: "+df[i]['symbol'] + "\tName: "+df[i]['name'])
            Ticker.objects.create(symbol=df[i]['symbol'], company=df[i]['name'])

            
   

#df.to_csv(r"path\ListOfAllSymbols.csv", index = True)


