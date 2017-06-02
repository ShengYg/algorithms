from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        maplist = [defaultdict(int) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                c2 = maplist[j][diff]
                res += c2
                maplist[i][diff] += c2+1
        return res
