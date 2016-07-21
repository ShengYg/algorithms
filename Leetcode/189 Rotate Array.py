class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[0:n-k] = nums[0:n-k][::-1]
        nums[n-k:n] = nums[n-k:n][::-1]
        nums[:] = nums[::-1]
        return
