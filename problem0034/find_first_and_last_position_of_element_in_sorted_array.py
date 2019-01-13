class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right, left = 0, 0
        low, high = 0, len(nums) - 1
        while low < high:
            mid = high - (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        right = high
        
        low = 0
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        left = low
        
        if len(nums) == 0 or nums[right] != target:
            return [-1,-1]
        else:
            return [left, right]      
                

        
