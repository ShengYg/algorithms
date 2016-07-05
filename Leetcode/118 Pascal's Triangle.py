class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = []
        for row in range(numRows):
            current = []
            for col in range(row+1):
                if col==0 or col==row:
                    current.append(1)
                else:
                    current.append(result[row-1][col-1]+result[row-1][col])
            result.append(current)

        return result
