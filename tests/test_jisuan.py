import unittest
from unittest.mock import patch
from Day05 import jisuan

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
    def test_add(self):
        with patch('builtins.input',side_effect=["0.0000001", "+ 0.0000002", "q"]):
            xiaoshu = jisuan.jisuanqi()
        self.assertAlmostEqual(xiaoshu,3e-7, places=8)
    def test_dividexiao(self):
        with patch('builtins.input',side_effect=["1", "/ 1e-10", "q"]):
            xiaoda = jisuan.jisuanqi()
        self.assertEqual(xiaoda, 1e+10)
if __name__=="__main__":
    unittest.main()  
