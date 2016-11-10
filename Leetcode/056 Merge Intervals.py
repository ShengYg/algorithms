# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key = lambda x:x.start)
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            if out[-1].end < intervals[i].start:
                out.append(intervals[i])
            if out[-1].end >= intervals[i].start:
                out[-1].end = max(intervals[i].end, out[-1].end)
        return out
