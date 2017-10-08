class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ret = []
        while n > 0:
            ret.append(n&1)
            n = n >> 1
        for i in range(1, len(ret)):
            if ret[i] == ret[i-1]:
                return False
        return True
