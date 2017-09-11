class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        ret = 0
        maxl = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                maxl += 1
            else:
                ret = max(ret, maxl)
                maxl = 1
        ret = max(ret, maxl)
        return ret
