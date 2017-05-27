class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.helper(nums, 0, len(nums)-1) >= 0
        
    def helper(self, nums, s, e):
        return nums[s] if s == e else max(nums[s] - self.helper(nums, s+1, e), nums[e] - self.helper(nums, s, e-1))

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = [[0] * len(nums) for _ in range(len(nums))]
        return self.helper(nums, 0, len(nums)-1, mem) >= 0
        
    def helper(self, nums, s, e, mem):
        if not mem[s][e]:
            mem[s][e] = nums[s] if s == e else max(nums[s] - self.helper(nums, s+1, e, mem), nums[e] - self.helper(nums, s, e-1, mem))
        return mem[s][e]
