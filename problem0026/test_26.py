import unittest

from .remove_duplicates_from_sorted_array import Solution

class TestRemoveDuplicates(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [1,1,2]
        output = 2
        self.assertEqual(s.removeDuplicates(input_list), output)

    def test_2(self):
        s = Solution()
        input_list = [0,0,1,1,1,2,2,3,3,4]
        output = 5
        self.assertEqual(s.removeDuplicates(input_list), output)        