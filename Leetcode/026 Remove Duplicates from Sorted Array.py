class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0 or m == 1:
            return m
        left = 0
        right = 1
        while right < m:
            while right < m and nums[right] == nums[left]:
                right = right + 1
            if right < m:
                dup = nums[right]
                left = left + 1
                nums[left] = dup
        return left + 1
