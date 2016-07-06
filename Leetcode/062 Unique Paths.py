class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        F = [[1 for _ in xrange(n)] for _ in xrange(m)]
        if n == 1 or m == 1:
            return 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                F[i][j] = F[i-1][j] + F[i][j-1]

        return F[m-1][n-1]
