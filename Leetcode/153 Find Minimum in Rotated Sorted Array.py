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
        return nums[lo]

    # if array is decreased
    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi)/2 + 1
            if nums[mid] > nums[lo]:
                hi = mid - 1
            elif nums[mid] < nums[lo]:
                lo = mid
        return nums[lo]
