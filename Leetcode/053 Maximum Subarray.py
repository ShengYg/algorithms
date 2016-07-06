class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        largest = max(nums)
        if largest <= 0:
            return largest
        
        current_max, current = 0, 0
        for i in range(len(nums)):
            if current + nums[i] > 0:
                current += nums[i]
            else:
                current = 0
            current_max = max(current_max, current)
        
        return current_max
