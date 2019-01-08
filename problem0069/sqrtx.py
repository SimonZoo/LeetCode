class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        another solution:
        return int(x**0.5)
        """
        low, high = 0, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                high = mid
            else:
                low = mid + 1
