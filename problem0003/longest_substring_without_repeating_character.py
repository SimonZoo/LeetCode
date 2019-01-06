class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i, c in enumerate(s):
            substring = c
            longest = max(1, longest)
            for n in s[i+1:]:
                if n in substring:
                    break
                else:
                    substring += n
                    longest = max(len(substring), longest)
        return longest
