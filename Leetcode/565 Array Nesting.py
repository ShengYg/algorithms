class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = [False] * len(nums)
        length = 0
        max_length = 0
        for i in range(len(nums)):
            if not A[i]:
                length = self.seti(nums, A, i)
                max_length = max(max_length, length)
        return max_length
        
    def seti(self, nums, A, i):
        sum_ = 0
        while not A[nums[i]]:
            A[nums[i]] = True
            i = nums[i]
            sum_ += 1
        return sum_
