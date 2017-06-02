class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = str(nums[0])
        if len(nums) == 1:
            return res
        if len(nums) == 2:
            return res + '/' + str(nums[1])
        res = res + '/(' +  str(nums[1])
        for i in range(2, len(nums)):
            res = res + '/' + str(nums[i])
        res += ')'
        return res
