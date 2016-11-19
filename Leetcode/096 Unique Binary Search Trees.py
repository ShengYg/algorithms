class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for _ in range(1 + n)]
        f[0], f[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                f[i] += f[j - 1] * f[i - j]
        return f[n]
