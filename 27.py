class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0 
        for i, n in enumerate(nums):
            if n != val:
                nums[j] = n
                j += 1
        return j
