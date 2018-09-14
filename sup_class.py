from __future__ import division
from stock import Stock
from user_commands import *

import datetime
import time
import pandas as pd

class SPTool:
  def __init__(self,stocks_csv='stocks.csv'):
    self.stock_dict = {}
    self.portfolio_df = 1
    self.load_stocks(stocks_csv)
    self.transaction_columns = ['Execution Time','Indicator','Symbol','Shares','Price']
    self.transactions_df = pd.DataFrame(columns=self.transaction_columns)

  def load_stocks(self,file_name):
    self.portfolio_df = pd.read_csv(file_name, sep=',',index_col='Symbol')
    for index, row in self.portfolio_df.iterrows():
      self.stock_dict[row['Symbol']] = Stock(row)
    self.portfolio_df['Shares'] = 0
    self.portfolio_df['VWSP'] = 0
    
  def get_vwsp(self,symb):
    return 10
  
  def refresh_portfolio(self):
    for index, stock_row in self.portfolio_df.iterrows():
      self.portfolio_df.at[index,'VWSP'] = lastp
  
  def get_a_pe_ratio(self,stock_symbol,price):
    return self.stock_dict[stock_symbol.upper()].p_e_ratio(price)

  def get_a_pe_ratio(self,stock_symbol,price):
    return self.stock_dict[stock_symbol.upper()].div_yield(price)

  def record_a_trade(self,ind,symb,shrs,pr,t_stamp=time.ctime()):
    self.transactions_df.loc[len(self.transactions_df)] = [t_stamp,ind,symb,shrs,pr]
    self.portfolio_df.at[index,'Shares'] += shrs if ind == "Buy" else -shrs
    self.portfolio_df.at[index,'VWSP'] = self.get_vwsp(symb)
    
    
    
    
