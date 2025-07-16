import unittest
import gongshi

class TestJisuanqi(unittest.TestCase):
    def test_add(self):
        self.assertEqual(gongshi.add(4, 5), 9)
    def test_substruct(self):
        self.assertEqual(gongshi.substruct(10, 5), 5)
    def test_multiply(self):
        self.assertEqual(gongshi.multiply(4, 5), 20)
    def test_divide(self):
        self.assertEqual(gongshi.divide(10, 4), 2.5)
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            gongshi.divide(5, 0)
if __name__ == "__main__":
    unittest.main()