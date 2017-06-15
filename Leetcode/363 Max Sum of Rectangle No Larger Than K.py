import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        res = -float('inf')
        for l in range(col):
            sums = [0] * row
            for r in range(l, col):
                for i in range(row):
                    sums[i] += matrix[i][r]
                curSum, curMax = 0, -float('inf')
                accu = [0]
                for s in sums:
                    curSum += s
                    u = bisect.bisect_left(accu, curSum - k)
                    if u < len(accu):
                        curMax = max(curMax, curSum - accu[u])
                    bisect.insort(accu, curSum)
                res = max(res, curMax)
        return res
