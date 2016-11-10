class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        out = [[]]
        for num in nums:
            out = out + [list + [num] for list in out]
        return out
