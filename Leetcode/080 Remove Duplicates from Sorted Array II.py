class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            count = 0
            while i+count<len(nums) and nums[i+count]==nums[i]:
                count += 1
            while count > 2:
                del nums[i + count - 1]
                count -= 1
            i += count
        return
