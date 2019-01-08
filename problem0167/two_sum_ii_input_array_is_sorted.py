class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # dict_nums = {}
        # for i, number in enumerate(numbers):
        #     p = target - number
        #     if p in dict_nums:
        #         return [dict_nums[p] + 1, i + 1]
        #     dict_nums[number] = i
        for i, number in enumerate(numbers):
            p = target - number
            low, high = i + 1, len(numbers) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] == p:
                    return [i + 1, mid + 1]
                elif numbers[mid] < p:
                    low = mid + 1
                else:
                    high = mid - 1
