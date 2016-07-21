class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sumA, i, minlen, numlen = 0, 0, float('inf'), len(nums)
        for j in range(len(nums)):
            sumA += nums[j]
            while sumA >= s:
                minlen = min(minlen, j - i + 1)
                sumA -= nums[i]
                i += 1
        return minlen if minlen <= numlen else 0
