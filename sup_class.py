from __future__ import division
from utils import *

from scipy.stats.mstats import gmean
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
    self.portfolio_df['VWSP'] = 0
    
  def get_vwsp(self,symb):
    five_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    self.transactions_df['Execution Time'] = pd.to_datetime(self.transactions_df['Execution Time']) 
    df = self.transactions_df.loc[(self.transactions_df['Execution Time'] >= five_min_ago) & (self.transactions_df['Symbol'] == symb)]
    try:
        return float((df["Price"] * df["Volume"]).sum() / df["Volume"].sum())
    except ZeroDivisionError:
        return df["Price"].mean()
  
  def get_GBCE_all_share_index():
    return gmean(self.portfolio_df.loc[:,"VWSP"])

  def get_a_dividend_yield(self,stock_symbol,price):
    if self.portfolio_df.at[stock_symbol,'Type'] == 'Common':
        dividend = self.portfolio_df.at[stock_symbol,'Last Dividend']
    else:
        dividend = self.portfolio_df.at[stock_symbol,'Fixed Dividend'] * self.portfolio_df.at[stock_symbol,'Par Value']
    return format(dividend / price, '.2f')

  def get_a_pe_ratio(self,stock_symbol,price):
    dividend = self.portfolio_df.at[stock_symbol,'Last Dividend']
    return format(price / dividend, '.2f')

  def record_a_trade(self,ind,symb,vol,pr,t_stamp=time.ctime()):
    self.transactions_df.loc[len(self.transactions_df)] = [t_stamp,ind,symb,vol,pr]
    self.portfolio_df.at[symb,'Shares'] += vol if ind == "Buy" else -vol
    self.portfolio_df.at[symb,'VWSP'] = self.get_vwsp(symb)
    
    
    
    