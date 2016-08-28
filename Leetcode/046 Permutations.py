class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.Recursive(nums, 0, result)
        return result

    def Recursive(self, nums, begin, result):
        if begin >= len(nums) - 1:
            result.append(nums)
            return
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.Recursive(nums[:], begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]


class Solution(object):
    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]


class Solution(object):
    def permute(self, nums):
        return map(list, itertools.permutations(nums))


