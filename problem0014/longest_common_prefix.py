class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        min_str = strs[0]
        for s in strs[1:]:
            if len(s) < len(min_str):
                min_str = s
                
        common = ''

        for i, c in enumerate(min_str):
            for s in strs:
                if s[i] != c:
                    return common
            common += c

        return common
