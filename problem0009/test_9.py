import unittest

from .palindrome_number import Solution

class TestNumber(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_num = 121
        output = True
        self.assertEqual(s.isPalindrome(input_num), output)
    
    def test_2(self):
        s = Solution()
        input_num = -121
        output = False
        self.assertEqual(s.isPalindrome(input_num), output)
    
    def test_3(self):
        s = Solution()
        input_num = 10
        output = False
        self.assertEqual(s.isPalindrome(input_num), output)