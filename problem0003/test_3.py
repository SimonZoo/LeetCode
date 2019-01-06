import unittest

from .longest_substring_without_repeating_character import Solution

class TestLongestSubstring(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_string = 'abcabcbb'
        out_put = 3
        self.assertEqual(s.lengthOfLongestSubstring(input_string), out_put)
    
    def test_2(self):
        s = Solution()
        input_string = 'bbbbbbb'
        out_put = 1
        self.assertEqual(s.lengthOfLongestSubstring(input_string), out_put)

    def test_3(self):
        s = Solution()
        input_string = ' '
        out_put = 1
        self.assertEqual(s.lengthOfLongestSubstring(input_string), out_put)
