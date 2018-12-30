class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: i nt
        :rtype: List[int]
        """
        nums_dict = {}
        for i, val in enumerate(nums):
            number = target - val
            if number in nums_dict:
                return [nums_dict[number], i]
            else:
                nums_dict[val]=i
