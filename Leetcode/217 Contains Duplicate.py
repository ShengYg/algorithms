class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nummap = {}
        for i in nums:
            if i in nummap:
                return True
            nummap[i] = nummap.get(i,0) + 1
        return False
