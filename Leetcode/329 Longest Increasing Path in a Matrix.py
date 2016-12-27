class Solution(object):
    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not len(matrix):
            return 0
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)]for _ in range(m)]
        maxlen = 1
        for i in range(m):
            for j in range(n):
                length = self.dfs(matrix, i, j, m, n, cache)
                maxlen = max(maxlen, length)
        return maxlen

    def dfs(self, matrix, i, j, m, n, cache):
        if cache[i][j]:
            return cache[i][j]
        maxlen = 1
        for item in self.dirs:
            y, x = i + item[0], j + item[1]
            if x < 0 or x >= n or y < 0 or y >= m or matrix[y][x] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(matrix, y, x, m, n, cache)
            maxlen = max(maxlen, length)
        cache[i][j] = maxlen
        return maxlen
