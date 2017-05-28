class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        maxtime, res = 0, 0
        for i in range(len(timeSeries)):
            if maxtime > timeSeries[i]:
                res += timeSeries[i] + duration - maxtime
            else:
                res += duration
            maxtime = timeSeries[i] + duration
        return res
