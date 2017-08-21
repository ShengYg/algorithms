class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(M), len(M[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s, cnt = 0, 0
                for move_i in [-1,0,1]:
                    for move_j in [-1,0,1]:
                        resi = i + move_i
                        resj = j + move_j
                        if resi >= 0 and resj >= 0 and resi < n and resj < m:
                            s += M[resi][resj]
                            cnt += 1
                res[i][j] = s / cnt
        return res
