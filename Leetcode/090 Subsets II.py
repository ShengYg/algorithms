class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        totalset = [[]]
        for num in nums:
            totalset += [i+[num] for i in totalset if i+[num] not in totalset]
        return totalset
