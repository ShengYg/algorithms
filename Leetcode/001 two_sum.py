class Solution(object):
    def twoSum(self, nums, target):
        sorted_num = sorted(nums)
        left = 0
        right = len(nums) - 1
        res = []
        while (left < right):
            sum = sorted_num[left] + sorted_num[right]
            if sum == target:
                break;
            elif sum > target:
                right -= 1
            else:
                left += 1
        if left == right:
            return -1, -1
        else:
            pos1 = nums.index(sorted_num[left])
            pos2 = nums.index(sorted_num[right])
            if pos1 == pos2:    # find again
                pos2 = nums[pos1 + 1:].index(sorted_num[right]) + pos1 + 1

            return min(pos1, pos2), max(pos1, pos2)
