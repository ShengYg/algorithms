class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)
        mini = float('inf')
        while lo < hi:
            mid = (lo + hi)/2
            mini = min(mini, nums[mid])
            if nums[lo] <= nums[mid] <= nums[hi-1]:
                return min(mini, nums[lo])
            elif nums[lo] > nums[mid] < nums[hi-1]:
                hi = mid
            else:
                lo = mid+1

        return mini
