class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach, edge, minstep = nums[0], 0, 0
        for i in range(1, len(nums)):
            if i > edge:
                minstep += 1
                edge = maxreach
                if edge > len(nums) - 1:
                    return minstep
            maxreach = max(maxreach, nums[i] + i)
            if maxreach == i and maxreach < len(nums) - 1:
                return -1
        return minstep

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach, edge, minstep, n = nums[0], 0, 0, len(nums)
        for i in range(1, n):
            if i > edge:
                minstep += 1
                edge = maxreach
                if edge >= n - 1:
                    return minstep
            maxreach = max(maxreach, nums[i] + i)
            if maxreach >= n - 1:
                return minstep + 1
        return minstep
