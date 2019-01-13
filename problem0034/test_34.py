import unittest

from .find_first_and_last_position_of_element_in_sorted_array import Solution

class TestFind(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [5,7,7,8,8,10]
        target = 8
        output = [3,4]
        self.assertEqual(s.searchRange(input_list, target), output)

    def test_2(self):
        s = Solution()
        input_list = [5,7,7,8,8,10]
        target = 6
        output = [-1,-1]
        self.assertEqual(s.searchRange(input_list, target), output)
    
    def test_3(self):
        s = Solution()
        input_list = [8,8,8,8,8,8]
        target = 8
        output = [0,5]
        self.assertEqual(s.searchRange(input_list, target), output)

    def test_4(self):
        s = Solution()
        input_list = []
        target = 0
        output = [-1,-1]
        self.assertEqual(s.searchRange(input_list, target), output)
       