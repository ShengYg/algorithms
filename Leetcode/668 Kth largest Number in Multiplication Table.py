class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l, h = 1, m*n
        while l != h:
            mid = (l + h)/ 2
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid/i, n)
            if cnt < k:
                l = mid + 1
            else:
                h = mid
        return h
