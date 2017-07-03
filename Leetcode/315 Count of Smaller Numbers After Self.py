from bisect import bisect_left
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        copy = sorted(nums)
        bit = [0] * (len(nums) + 1)
        for item in nums[::-1]:
            idx = bisect_left(copy, item)
            res.append(self.search(bit, idx))
            self.insert(bit, idx + 1)
        return res[::-1]

    def search(self, bit, i):
        sum = 0
        while i > 0:
            sum += bit[i]
            i -= i & -i
        return sum

    def insert(self, bit, i):
        while i < len(bit):
            bit[i] += 1
            i += i & -i
