class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        A = [0] * (rowIndex + 1)
        A[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                A[j] += A[j - 1]
        return A
