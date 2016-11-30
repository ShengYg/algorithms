class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = [0 for _ in range(len(s) + 1)]
        count[-1] = 1
        count[-2] = 0 if s[-1] == '0' else 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                continue
            count[i] = count[i+1] + count[i+2] if int(s[i:i+2])<27 else count[i+1]
        return count[0]
