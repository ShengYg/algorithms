class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 1
        max_num = -float('inf')
        for i in range(len(nums)):
            out *= nums[i]
            max_num = max(out, max_num)
            if nums[i] == 0:
                out = 1
        out = 1
        for i in range(len(nums)-1, -1, -1):
            out *= nums[i]
            max_num = max(out, max_num)
            if nums[i] == 0:
                out = 1
        return max_num
