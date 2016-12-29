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
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) > 2:
            out = [0 for _ in range(len(nums))]
            out[0] = nums[0]
            out[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                out[i] = max(nums[i] + out[i - 2], out[i - 1])
            return out[-1]



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        out = [0, 0]
        for i in range(len(nums)):
            a, b = out[0], out[1]
            out[0] = b + nums[i]
            out[1] = max(a, b)
        return max(out)
