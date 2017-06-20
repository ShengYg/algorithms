class Solution(object):
    def findPaths(self, m, n, N, y, x):
        """
        :type m: int
        :type n: int
        :type N: int
        :type y: int
        :type x: int
        :rtype: int
        """
        if N == 0:
            return 0
        mem = [[[1]*(n+2)for _ in range(m+2)] for _ in range(N)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mem[0][i][j] = 0
        for step in range(1, N):
            for i in range(1, m+1):
                for j in range(1, n+1):
                    mem[step][i][j] = (mem[step-1][i-1][j] + mem[step-1][i+1][j] + mem[step-1][i][j-1] + mem[step-1][i][j+1]) % 1000000007
        return (mem[N-1][y][x+1] + mem[N-1][y+2][x+1] + mem[N-1][y+1][x] + mem[N-1][y+1][x+2]) % 1000000007
