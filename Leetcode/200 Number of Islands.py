class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        out = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                out += self.sink(grid, i, j)
        return out

    def sink(self, grid, i, j):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.sink(grid, i + 1, j)
        self.sink(grid, i - 1, j)
        self.sink(grid, i, j + 1)
        self.sink(grid, i, j - 1)
        return 1
