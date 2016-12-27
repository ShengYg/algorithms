class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                out.append(abs(index + 1))
            nums[index] = -nums[index]
        return out
