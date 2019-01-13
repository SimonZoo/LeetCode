import unittest

from .search_a_2d_matrix import Solution
    
class TestSearch(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [
                [1,   3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
                ]
        target = 3
        output = True
        self.assertEqual(s.searchMatrix(input_list, target), output)
    
    def test_2(self):
        s = Solution()
        input_list = [
                [1,   3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
                ]
        target = 13
        output = False
        self.assertEqual(s.searchMatrix(input_list, target), output)

    def test_3(self):
        s = Solution()
        input_list = []
        target = 0
        output = False
        self.assertEqual(s.searchMatrix(input_list, target), output)
    
    def test_4(self):
        s = Solution()
        input_list = [[],[]]
        target = 1
        output = False
        self.assertEqual(s.searchMatrix(input_list, target), output)

    def test_5(self):
        s = Solution()
        input_list = [[1]]
        target = 2
        output = False
        self.assertEqual(s.searchMatrix(input_list, target), output)
    
    def test_6(self):
        s = Solution()
        input_list = [[1]]
        target = 1
        output = True
        self.assertEqual(s.searchMatrix(input_list, target), output)

    def test_7(self):
        s = Solution()
        input_list = [
                [1,   3,  5,  7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
                ]
        target = 10
        output = True
        self.assertEqual(s.searchMatrix(input_list, target), output)
    
    