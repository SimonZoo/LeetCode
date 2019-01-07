import unittest

from .longest_common_prefix import Solution

class TestCommonPrefix(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = ["flower","flow","flight"]
        output = "fl"
        self.assertEqual(s.longestCommonPrefix(input_list), output)

    def test_2(self):
        s = Solution()
        input_list = ["dog","racecar","car"]
        output = ""
        self.assertEqual(s.longestCommonPrefix(input_list), output)
    
    def test_3(self):
        s = Solution()
        input_list = []
        output = ""
        self.assertEqual(s.longestCommonPrefix(input_list), output)

    def test_4(self):
        s = Solution()
        input_list = ["dog"]
        output = "dog"
        self.assertEqual(s.longestCommonPrefix(input_list), output)
        