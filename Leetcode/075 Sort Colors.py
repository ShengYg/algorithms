class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        zero, two = 0, len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
