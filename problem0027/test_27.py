import unittest

from .remove_element import Solution

class TestRemoveElement(unittest.TestCase):
    def test_1(self):
        s = Solution()
        input_list = [3,2,2,3]
        val = 3
        output = 2
        self.assertEqual(s.removeElement(input_list, val), output)
    
    def test_2(self):
        s = Solution()
        input_list = [0,1,2,2,3,0,4,2]
        val = 2
        output = 5
        self.assertEqual(s.removeElement(input_list, val), output)