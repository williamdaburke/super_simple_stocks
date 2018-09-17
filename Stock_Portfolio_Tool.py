from __future__ import division
from utils import *
from scipy.stats.mstats import gmean

import pdb
import datetime
import time
import pandas as pd
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

class Stock_Portfolio_Tool:
  def __init__(self,stocks_csv='data/stocks.csv'):
    self.load_stocks(stocks_csv)
    self.transaction_columns = ['Execution Time','Indicator','Symbol','Volume','Price']
    self.transactions_df = pd.DataFrame(columns=self.transaction_columns)

  def load_stocks(self,file_name):
    self.portfolio_df = pd.read_csv(file_name, sep=',',index_col='Symbol')
    self.portfolio_df['Shares'] = 0
    self.portfolio_df['VWSP'] = None
    
  def get_vwsp(self,symb):
    time_limit = minutes_ago(5)
    self.transactions_df['Execution Time'] = pd.to_datetime(self.transactions_df['Execution Time']) 
    df = self.transactions_df.loc[(self.transactions_df['Execution Time'] >= time_limit) & (self.transactions_df['Symbol'] == symb.upper())]
    if df.shape[0] > 0:
      return wavg(df,"Price","Volume")
    else:
      #depends on whether stocks with no trades in last 5mins should have Volume Weighted Stock Price set at 0 or left unchanged since last calculation. If a trade is recorded which was executed 30 mins ago and has had no trades since then (i.e. in last five minutes), what should VWSP be?
      return None #self.portfolio_df.at[symb,'VWSP']
  
  def get_GBCE_all_share_index(self):
    a = np.array(self.portfolio_df.loc[self.portfolio_df['VWSP'] > 0]['VWSP'])
    return geomean(a)

  def get_a_dividend_yield(self,stock_symbol,price):
    stock_symbol = stock_symbol.upper()
    if self.portfolio_df.at[stock_symbol,'Type'] == 'Common':
        dividend = self.portfolio_df.at[stock_symbol,'Last Dividend']
    else:
        dividend = self.portfolio_df.at[stock_symbol,'Fixed Dividend'] * self.portfolio_df.at[stock_symbol,'Par Value']
    return format(dividend / price, '.2%')

  def get_a_pe_ratio(self,stock_symbol,price):
    dividend = self.portfolio_df.at[stock_symbol.upper(),'Last Dividend']
    return price / dividend

  def record_a_trade(self,ind,symb,vol,pr,t_stamp=datetime.datetime.now()):
    symb = symb.upper() 
    ind = cap(ind)
    self.transactions_df.loc[len(self.transactions_df)] = [t_stamp,ind,symb,vol,pr]
    self.portfolio_df.at[symb,'Shares'] += vol if ind == "Buy" else -vol
    self.portfolio_df.at[symb,'VWSP'] = self.get_vwsp(symb)
    
    
    
    