from __future__ import division

class Stock:
    def __init__(self,stock_line):
        self.symbol = stock_line['Symbol']
        self.stock_type = stock_line['Type']
        self.last_dividend = stock_line['Last Dividend']
        self.fixed_dividend = stock_line['Fixed Dividend']
        self.par_value = stock_line['Par Value']
        if self.stock_type == "Common":
            self.dividend = self.last_dividend
        else :
            self.dividend = self.fixed_dividend * self.par_value
        
    def div_yield(self,price):
        return self.dividend / price
    
    def p_e_ratio(self,price):
        return price / self.dividend


      