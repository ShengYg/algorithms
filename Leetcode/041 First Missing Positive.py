class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            cur = nums[i]
            if cur >= 0 and cur < n and nums[cur] != nums[i]:
                nums[i], nums[cur] = nums[cur], nums[i]
            else:
                i += 1
        k = 1
        while k < n and nums[k] == k:
            k += 1
        if n == 0 or k < n:
            return k
        else:
            return nums[0] == k and k + 1 or k
