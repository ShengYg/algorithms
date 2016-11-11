# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
                newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
                intervals.remove(intervals[i])
        intervals.insert(i, newInterval)
        return intervals
