class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            res.append(chr((n - 1) % 26 + 65))
            (n - 1) /= 26
        return ''.join(res[::-1])
