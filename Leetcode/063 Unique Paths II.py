class Solution(object):
### method 1
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0

        path = [[0 for _ in range(n)] for _ in range(m)]
        path[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i==0:
                    path[i][j] = path[i][j-1] if obstacleGrid[i][j-1]==0 else 0
                elif j==0:
                    path[i][j] = path[i-1][j] if obstacleGrid[i-1][j]==0 else 0
                else:
                    if obstacleGrid[i][j-1]==0 and obstacleGrid[i-1][j]==0:
                        path[i][j] = path[i-1][j]+path[i][j-1]
                    elif obstacleGrid[i][j-1]==0:
                        path[i][j] = path[i][j-1]
                    elif obstacleGrid[i-1][j]==0:
                        path[i][j] = path[i-1][j]
                    else:
                        path[i][j]=0


        return path[m-1][n-1]

### method 2
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] * 1
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] * 1
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[m-1][n-1]
