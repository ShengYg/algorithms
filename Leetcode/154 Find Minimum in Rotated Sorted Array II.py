class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi)/2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi -= 1
        return nums[lo]


    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)/2		#faster
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi -= 1
        return nums[lo]
