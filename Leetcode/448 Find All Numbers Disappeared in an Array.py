class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums:
            val = abs(num) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(len(nums)):
            if nums[i] > 0:
                out.append(i + 1)
        return out
