import unittest

from .two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [2, 7, 11, 15]
        target = 9
        output_list = [0, 1]
        self.assertEqual(s.twoSum(input_list, target), output_list)
