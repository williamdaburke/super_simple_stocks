from __future__ import division
from stock import Stock
from user_commands import *

import pandas as pd

stock_dict = {}

def get_a_pe_ratio():
  print stock_dict[ask_symbol()].p_e_ratio(ask_price())
  
def div_y():
  print stock_dict[ask_symbol()].div_yield(ask_price())
    
def perform_trade():
  indicator = raw_input('please choose Buy or Sell \n --->')
  symbol = ask_symbol()
  price = ask_price()
  
  
def vol_wei_stock_p():
  indicator = raw_input('please choose Buy or Sell \n --->')
  symbol = ask_symbol()
  price = ask_price()

def gbce_all_share_index():
  indicator = raw_input('please choose Buy or Sell \n --->')
  symbol = ask_symbol()
  price = ask_price()

initial_choices = {
      1 : get_a_pe_ratio,   
      2 : div_y,
      3 : perform_trade,
      4 : vol_wei_stock_p,
      5 : gbce_all_share_index
    }
  
if __name__== "__main__":
  df = pd.read_csv('stocks.csv', sep=',')
  for index, row in df.iterrows():
      stock_dict[row['Symbol']] = Stock(row)
  
  request_num = raw_input("Press: \n 1. to check a P/E ratio. \n 2. to check a dividen yield. \n 3. record a trade. \n 4. calculate Volume Weighted Stock Price based on trades in past 5 minutes. \n \n  --->")
  
  initial_choices[int(request_num)]()
  