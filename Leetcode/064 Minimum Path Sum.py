class Solution(object):
### method 1 84ms
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[m-1][n-1]

### method 2 72ms
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[0][j] = grid[0][j-1] + grid[0][j]
                elif j == 0:
                    grid[i][0] = grid[i-1][0] + grid[i][0]
                else:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        
        return grid[m-1][n-1]
