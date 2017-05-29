from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_all = 0
        for i in range(len(nums)):
            sum_all += nums[i]
            nums[i] = 2 * sum_all - i - 1
        d = defaultdict(list)
        for i, k in enumerate(nums):
            d[k].append(i)
        res = 0
        for k, i in d.items():
            if k == 0:
                res = max(res, max(i)+1)
            res = max(res, max(i) - min(i))
        return res


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length
