class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robsub(nums, 0, len(nums) - 1), self.robsub(nums, 1, len(nums)))
        
    def robsub(self, nums, start, end):
        if not nums:
            return 0
        out = [0, 0]
        for i in range(start, end):
            a, b = out[0], out[1]
            out[0] = b + nums[i]
            out[1] = max(a, b)
        return max(out)
