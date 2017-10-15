class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        height, l, r = [], [], []
        res = 0
        ret = []
        for i in range(len(positions)):
            l.append(positions[i][0])
            r.append(positions[i][0] + positions[i][1] - 1)
            height.append(0)
            for j in range(i - 1, -1, -1):
                if r[i] < l[j] or r[j] < l[i]:
                    continue
                height[i] = max(height[i], height[j])
            height[i] += positions[i][1]
            res = max(res, height[i])
            ret.append(res)
        return ret
