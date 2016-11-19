class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        out = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and out != 0:
                break
            if s[i] != ' ':
                out += 1
        return out
