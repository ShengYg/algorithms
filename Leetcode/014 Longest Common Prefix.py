class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs)
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]
        a, b, j = strs[0], strs[length - 1], -1
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                j = i
            else:
                break
        return a[:j + 1]
