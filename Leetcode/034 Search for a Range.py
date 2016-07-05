class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = []
        length = len(nums)

        # low-bound binary search
        start = 0
        end = length  # [0, length)
        while start<end:
            mid = (start+end)/2
            if nums[mid]<target:  # NOTICE: less than
                start = mid+1
            else:
                end = mid

        if start<length and nums[start]==target:
            result.append(start)
        else:
            return [-1, -1]
            
        start = start
        end = length  # no "-1" # [0, length)
        while start<end:
            mid = (start+end)/2
            if nums[mid]<=target:  # NOTICE: less than or equal
                start = mid+1
            else:
                end = mid

        result.append(start-1)
        return result
