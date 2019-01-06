class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        i = 0
        while i < len(nums):
            if nums[i] in nums_dict:
                nums.pop(i)
            else:
                nums_dict[nums[i]] = i
                i = i + 1
        return len(nums)
