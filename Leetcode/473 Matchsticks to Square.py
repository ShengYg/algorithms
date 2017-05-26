class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False
        if sum(nums) % 4 != 0:
            return False
        sums = [0] * 4
        nums = sorted(nums)[::-1]
        return self.dfs(nums, sums, 0, sum(nums) / 4)

    def dfs(self, nums, sums, index, target):
        if index == len(nums):
            if sums[0] == target and sums[1] == target and sums[2] == target and sums[3] == target:
                return True
            else:
                return False
        for i in range(4):
            if sums[i] + nums[index] > target:
                continue
            j = i - 1
            while j >= 0:
                j -= 1
                if sums[i] == sums[j]:
                    break
            if j != -1:
                continue
            sums[i] += nums[index]
            if self.dfs(nums, sums, index + 1, target):
                return True
            sums[i] -= nums[index]
        return False
