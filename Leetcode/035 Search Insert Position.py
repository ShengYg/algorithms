class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        if not nums or length == 0:
            return 0
        
        start, end = 0, length
        while start < end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
                
        return start
