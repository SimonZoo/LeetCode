class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        y = 0
        if x < 0:
            flag = True
            x = -x
        while x > 0:
            last = x % 10
            y = y * 10 + last
            x = x // 10
        
        if flag:
            y = -y
        if y > (1 << 31)-1 or y < -(1 << 31):
            y = 0
        return y
