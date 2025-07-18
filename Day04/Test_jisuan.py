import unittest
from unittest.mock import patch
import jisuan

class Testjisuan(unittest.TestCase):

    def test_jisuan(self):
         with patch('builtins.input',side_effect=["2","+ 3","* 5","q"]):
             result = jisuan.jisuanqi()
         self.assertEqual(result, 25)  
    def test_divide(self):
         with patch('builtins.input',side_effect=["2","oi"]):
             cuowu= jisuan.jisuanqi()
         self.assertIsNone(cuowu)
    def test_weiling(self):
         with patch('builtins.input',side_effect=["2","0"]):
             ling= jisuan.jisuanqi()
         self.assertIsNone(ling)
if __name__=="__main__":
    unittest.main()  