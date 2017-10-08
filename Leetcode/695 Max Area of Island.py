class Solution(object):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ret = max(self.dfs(i, j, m, n, grid), ret)
        return ret

    def dfs(self, row, col, m, n, grid):
        ret = 1
        for dir in self.dirs:
            i = row + dir[0]
            j = col + dir[1]
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                ret += self.dfs(i, j, m, n, grid)
        return ret
