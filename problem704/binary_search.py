class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def b_s(start, end, t):
            mid = (end + start) // 2
            if nums[mid] == t:
                return mid

            if end <= start:
                return -1

            if nums[mid] > t:
                return b_s(start, mid-1, t)
            else:
                return b_s(mid+1, end, t)
            
        return b_s(0, len(nums)-1, target)