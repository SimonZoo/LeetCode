class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        y = 0
        xx = x
        while x != 0:
            t = x % 10
            y = y * 10 + t
            x = x // 10
        return y == xx
