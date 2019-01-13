class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        low, high = 0, len(matrix) - 1
        while low < high:
            mid = high - (high - low) // 2

            if len(matrix[low]) == 0:
                return False

            if matrix[mid][0] < target:
                low = mid
            elif matrix[mid][0] > target:
                high = mid - 1                
            else:
                return True

        i, j = 0, len(matrix[low]) - 1
        while i <= j:
            # m = i + (j - i) // 2
            m = j - (j - i) // 2
            if matrix[low][m] > target:
                j = m - 1
            elif matrix[low][m] < target:
                i = m + 1
            else:
                return True
        return False
        
