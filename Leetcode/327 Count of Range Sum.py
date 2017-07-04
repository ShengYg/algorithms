from bisect import bisect_left
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0
        return self.countRangeSumSub(nums, 0, len(nums) - 1, lower, upper)

    def countRangeSumSub(self, nums, l, r, lower, upper):
        if l == r:
            return 1 if nums[l] >= lower and nums[r] <= upper else 0
        m = l + (r - l) / 2
        arr = [0] * (r - m)
        sum_num = 0
        count = 0

        for i in range(m+1, r+1):
            sum_num += nums[i]
            arr[i - m - 1] = sum_num

        arr = sorted(arr)
        sum_num = 0
        for i in range(m, l-1, -1):
            sum_num += nums[i]
            count += bisect_left(arr, upper - sum_num + .5) - bisect_left(arr, lower - sum_num - .5)

        return self.countRangeSumSub(nums, l, m, lower, upper) + self.countRangeSumSub(nums, m+1, r, lower, upper) + count

from bisect import bisect_left
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0
        n = len(nums)
        sums = [0] * n
        sum_num = 0
        for i in range(n):
            sum_num += nums[i]
            sums[i] = sum_num
        return self.countRangeSumSub(sums, 0, n-1, lower, upper)

    def countRangeSumSub(self, sums, start, end, lower, upper):
        if start == end:
            return 1 if sums[start] >= lower and sums[end] <= upper else 0
        mid = (start + end) / 2
        a = self.countRangeSumSub(sums, start, mid, lower, upper)
        b = self.countRangeSumSub(sums, mid+1, end, lower, upper)
        count = a + b

        j, k, t = mid+1, mid+1, mid+1
        cache = [0] * (end - start + 1)
        r = 0
        for i in range(start, mid+1):
            while k <= end and sums[k] - sums[i] < lower:
                k += 1
            while j <= end and sums[j] - sums[i] <= upper:
                j += 1
            while t <= end and sums[t] < sums[i]:
                cache[r] = sums[t]
                r += 1
                t += 1
            cache[r] = sums[i]
            count += j - k
            r += 1
        sums[start:t] = cache[0:t-start]
        return count
