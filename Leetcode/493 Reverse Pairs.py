# BIT
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

# merge sort
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.reversePairsSub(nums, 0, len(nums) - 1)
    
    def reversePairsSub(self, nums, l, r):
        if l >= r:
            return 0
        m = l + ((r - l) >> 1);
        res = self.reversePairsSub(nums, l, m) + self.reversePairsSub(nums, m + 1, r)
        
        i, k, j, p = l, 0, m+1, m+1
        merge = [0] * (r-l+1)
        while i <= m:
            while p <= r and nums[i] > 2 * nums[p]:
                p += 1
            res += p - (m + 1)
            
            while j <= r and nums[i] >= nums[j]:
                merge[k] = nums[j]
                k += 1
                j += 1
            merge[k] = nums[i]
            k += 1
            i += 1
        while j <= r:
            merge[k] = nums[j]
            k += 1
            j += 1
        nums[l:r+1] = merge
        return res
