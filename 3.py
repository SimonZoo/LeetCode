class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i, c in enumerate(s):
            substring = c
            for n in s[i+1:]:
                if n in substring:
                    longest = max(len(substring), longest)
                    break
                else:
                    substring += n
        return longest
