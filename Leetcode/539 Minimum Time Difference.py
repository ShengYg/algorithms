class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        bucket = [0] * 60 * 24
        for time in timePoints:
            hour, minute = time.split(':')
            hour = int(hour)
            minute = int(minute)
            if bucket[hour*60+minute]:
                return 0
            else:
                bucket[hour*60+minute] = 1
        prev, min_ = 0, float('inf')
        first, last = float('inf'), -float('inf')
        for i in range(0, 60 * 24):
            if bucket[i]:
                if first != float('inf'):
                    min_ = min(min_, i-prev)
                first = min(first, i)
                last = max(last, i)
                prev = i
        min_ = min(min_, (24 * 60 - last + first))
        return min_
