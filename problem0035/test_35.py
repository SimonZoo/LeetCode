import unittest

from .search_insert_position import Solution

class TestSearchInsertPosition(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [1,3,5,6]
        target = 5
        output = 2
        self.assertEqual(s.searchInsert(input_list, target), output)

    def test_2(self):
        s = Solution()
        input_list = [1,3,5,6]
        target = 2
        output = 1
        self.assertEqual(s.searchInsert(input_list, target), output)

    def test_3(self):
        s = Solution()
        input_list = [1,3,5,6]
        target = 7
        output = 4
        self.assertEqual(s.searchInsert(input_list, target), output)

    def test_4(self):
        s = Solution()
        input_list = [1,3,5,6]
        target = 0
        output = 0
        self.assertEqual(s.searchInsert(input_list, target), output)
