import unittest

from .sqrtx import Solution

class TestSqrt(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_n = 4
        output = 2
        self.assertEqual(s.mySqrt(input_n), output)

    def test_2(self):
        s = Solution()
        input_n = 8
        output = 2
        self.assertEqual(s.mySqrt(input_n), output)