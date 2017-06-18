class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(machines) % len(machines):
            return -1
        ave = sum(machines) / len(machines)
        cnt, maxval = 0, 0
        for load in machines:
            cnt += load - ave
            maxval = max(max(maxval, abs(cnt)), load - ave)
        return maxval
