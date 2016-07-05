class Solution:
### method 1
    def rotate(self, matrix):
		"""
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

### method 2
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for col in range(n-row):
                matrix[row][col], matrix[n-1-col][n-1-row] = matrix[n-1-col][n-1-row], matrix[row][col]
        for row in range(n/2):
            for col in range(n):
                matrix[row][col], matrix[n-1-row][col] = matrix[n-1-row][col], matrix[row][col]

        return
