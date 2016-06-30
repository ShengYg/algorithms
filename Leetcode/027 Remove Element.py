class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == val:
                right = right + 1
            else:
                nums[left] = nums[right]
                left = left + 1
                right = right + 1
        return left
            
