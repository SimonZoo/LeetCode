import unittest

from .reverse_integer import Solution

class TestReverse(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_int = 123
        output = 321
        self.assertEqual(s.reverse(input_int), output)
    
    def test_2(self):
        s = Solution()
        input_int = -123
        output = -321
        self.assertEqual(s.reverse(input_int), output)

    def test_3(self):
        s = Solution()
        input_int = 120
        output = 21
        self.assertEqual(s.reverse(input_int), output)
    