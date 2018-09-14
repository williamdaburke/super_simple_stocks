from __future__ import division
from stock import Stock
from user_commands import *

import time
import pandas as pd

stock_dict = {}

transaction_columns = ['Execution Time','Symbol','Price']
transactions_df = pd.DataFrame(columns=transaction_columns)

def load_stock_dict(file_name='stocks.csv'):
  df = pd.read_csv(file_name, sep=',')
  for index, row in df.iterrows():
      stock_dict[row['Symbol']] = Stock(row)

def get_a_pe_ratio(stock_symbol,price):
  return stock_dict[stock_symbol].p_e_ratio(price)

def get_a_pe_ratio(stock_symbol,price):
  return stock_dict[stock_symbol].div_yield(price)
      
def record_a_trade(symb,quantity,indicator,price,time_stamp=time.time())
  