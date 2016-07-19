class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        maxA = 0
        for i in range(m):
            lcur, rcur = 0, n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], rcur)
                else:
                    right[j] = n
                    rcur = j
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], lcur)
                else:
                    height[j] = 0
                    left[j] = 0
                    lcur = j + 1
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA
