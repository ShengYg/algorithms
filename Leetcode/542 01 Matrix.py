import sys
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = sys.maxint
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while len(queue):
            cell = queue.pop(0)
            for d in dirs:
                a = cell[0] + d[0]
                b = cell[1] + d[1]
                if a < 0 or a >= m or b < 0 or b >= n or matrix[a][b] <= matrix[cell[0]][cell[1]] + 1:
                    continue
                matrix[a][b] = matrix[cell[0]][cell[1]] + 1
                queue.append((a, b))
        return matrix
            
