class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1, l2 = len(haystack), len(needle)
        if l2 == 0:
            return 0
        for i in range(l1 - l2 + 1):
            for j in range(l2 + 1):
                if j == l2:
                    return i
                if needle[j] != haystack[i + j]:
                    break
        return -1
