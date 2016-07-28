class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        index = n - 1
        while index > 0:
            if nums[index - 1] < nums[index]:
                break
            index -= 1
        if index == 0:
            nums.reverse()
            return
        val, j = nums[index - 1], n - 1
        while j >= index:
            if nums[j] > val:
                break
            j -= 1
        nums[j], nums[index - 1] = nums[index - 1], nums[j]
        nums[index:n] = nums[index:n][::-1]
        return
