# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        l = sorted((inter.start, i) for i, inter in enumerate(intervals))
        res = []
        for inter in intervals:
            pos = bisect.bisect_left(l, (inter.end, ))
            res.append(l[pos][1] if pos < len(l) else -1)
        return res
