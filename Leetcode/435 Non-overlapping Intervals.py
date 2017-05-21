# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        sort_intervals = sorted(intervals, key = lambda x: x.end)
        end = float('-inf')
        erased = 0
        for inter in sort_intervals:
            if inter.start >= end:
                end = inter.end
            else:
                erased += 1
        return erased
