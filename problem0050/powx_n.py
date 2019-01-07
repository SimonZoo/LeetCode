class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        
        f = 1
        while n:
            if n % 2 == 1:
                f = f * x
            x = x * x
            n = n // 2
        return f 
        