import unittest

from .powx_n import Solution

class TestPowx(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_x = 2.00000
        input_n = 10
        output = 1024.00000
        self.assertAlmostEqual(s.myPow(input_x, input_n), output)
    
    def test_2(self):
        s = Solution()
        input_x = 2.10000
        input_n = 3
        output = 9.26100
        self.assertAlmostEqual(s.myPow(input_x, input_n), output)
    
    def test_3(self):
        s = Solution()
        input_x = 2.00000
        input_n = -2
        output = 0.25000
        self.assertAlmostEqual(s.myPow(input_x, input_n), output)
    
    def test_4(self):
        s = Solution()
        input_x = -2.00000
        input_n = 2
        output = 4.0
        self.assertAlmostEqual(s.myPow(input_x, input_n), output)