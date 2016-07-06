class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        reachable = 0
        for i in range(0, len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True
        
