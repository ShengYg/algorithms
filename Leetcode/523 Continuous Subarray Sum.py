from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        map = defaultdict(lambda: None)
        map[0] = -1
        runningsum = 0
        for i in range(len(nums)):
            runningsum += nums[i]
            runningsum %= k
            prev = map[runningsum]
            if prev is not None:
                if i - prev > 1:
                    return True
            else:
                map[runningsum] = i
        return False

