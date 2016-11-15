class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        p = triangle[len(triangle) - 1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, i + 1):
                p[j] = min(p[j + 1], p[j]) + triangle[i][j]
        return p[0]
