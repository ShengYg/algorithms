class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        out = []
        i = 0
        while i < len(nums):
            a = nums[i]
            while i+1 < len(nums) and nums[i+1]-nums[i]==1:
                i += 1
            if a == nums[i]:
                out.append(str(a))
            else:
                out.append(str(a) + "->" + str(nums[i]))
            i += 1
        return out
