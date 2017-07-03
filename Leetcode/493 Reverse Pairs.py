from bisect import bisect_left
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        copy = sorted(nums)
        bit = [0] * (len(nums) + 1)
        for item in nums:
            res += self.search(bit, bisect_left(copy, 2*item+1) + 1)
            self.insert(bit, bisect_left(copy, item) + 1)
        return res
    
    def search(self, bit, i):
        sum = 0
        while i < len(bit):
            sum += bit[i]
            i += i & -i
        return sum
    
    def insert(self, bit, i):
        while i > 0:
            bit[i] += 1
            i -= i & -i
