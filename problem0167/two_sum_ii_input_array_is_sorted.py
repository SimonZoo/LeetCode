class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for i, number in enumerate(numbers):
            p = target - number
            if p in dict_nums:
                return [dict_nums[p] + 1, i + 1]
            dict_nums[number] = i
