import unittest

from .binary_search import Solution

class TestBinarySearch(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [-1,0,3,5,9,12]
        target = 9
        output = 4
        self.assertEqual(s.search(input_list, target), output)

    def test_2(self):
        s = Solution()
        input_list = [-1,0,3,5,9,12]
        target = 2
        output = -1
        self.assertEqual(s.search(input_list, target), output)

    def test_3(self):
        s = Solution()
        input_list = [5]
        target = 5
        output = 0
        self.assertEqual(s.search(input_list, target), output)