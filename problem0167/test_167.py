import unittest 

from .two_sum_ii_input_array_is_sorted import Solution

class TestTwoSum(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [2,7,11,15]
        target = 9
        output = [1,2]
        self.assertEqual(s.twoSum(input_list, target), output)

    def test_2(self):
        s = Solution()
        input_list = [2,3,4]
        target = 6
        output = [1,3]
        self.assertEqual(s.twoSum(input_list, target), output)
    
    def test_3(self):
        s = Solution()
        input_list = [0,0,3,4]
        target = 0
        output = [1,2]
        self.assertEqual(s.twoSum(input_list, target), output)
        
        