class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix or not matrix[0]:
            return matrix

        result = []

        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        while left<=right and top<=bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])
            for i in range(right-1, left, -1):
                if top<bottom:
                    result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                if left<right:
                    result.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result
