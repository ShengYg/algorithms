class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 1, 1
        for i in range(2, n+1):
            a = a + b
            b = a - b
        return a
