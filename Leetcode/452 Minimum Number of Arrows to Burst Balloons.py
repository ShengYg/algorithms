class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        end = -float('inf')
        res = 0
        for s in sorted(points, key=lambda x: x[1]):
            if s[0] > end:
                end = s[1]
                res += 1
        return res
