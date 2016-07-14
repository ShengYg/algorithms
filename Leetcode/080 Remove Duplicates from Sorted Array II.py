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

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
