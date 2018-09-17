from __future__ import division
from utils import *
import unittest
from Stock_Portfolio_Tool import Stock_Portfolio_Tool

class TestCases(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCases, self).__init__(*args, **kwargs)
        self.stp = Stock_Portfolio_Tool()
        self.stp.record_a_trade('Buy','GIN',25,71,minutes_ago(4))
        self.stp.record_a_trade('SELL','gin',7,87)
        self.stp.record_a_trade('buy','tea',15,20)
        self.stp.record_a_trade('BUY','GIN',55,55,minutes_ago(10))
        self.stp.record_a_trade('Sell','GIN',7,85,minutes_ago(13))
        self.stp.record_a_trade('Buy','TEA',40,25)
        self.stp.record_a_trade('Buy','TEA',50,21)
        self.stp.record_a_trade('Buy','tea',70,29)
        self.stp.record_a_trade('Buy','TEA',37,23)
        self.stp.record_a_trade('buy','GIN',45,77)
        self.stp.record_a_trade('sell','GIN',37,87)
        self.stp.record_a_trade('bUY','Tea',20,10)
        self.stp.record_a_trade('Buy','ale',20,10)
        self.stp.record_a_trade('bUY','pop',44,40,minutes_ago(30))
        self.stp.record_a_trade('bUY','pop',44,40,minutes_ago(31))
        self.stp.record_a_trade('BUY','JOE',30,30)
        #print self.stp.portfolio_df
    
    def test_pe_ratio(self):
        self.assertEqual(self.stp.get_a_pe_ratio('POP',70),8.75)
    
    def test_div_yield(self):
        self.assertEqual(self.stp.get_a_dividend_yield('GIN',80),'2.50%')
        
    def test_vwsp(self):    
        self.assertEqual(self.stp.get_vwsp('tea'),23.409)
        
    def test_gbce(self):    
        self.assertEqual(self.stp.get_GBCE_all_share_index(),27.339)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)