cache = {}
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i, X):
            if i == 1:
                return 1
            key = i, X
            if key in cache:
                return cache[key]
            total = sum(helper(i - 1, X[:j] + X[j + 1:])
                        for j, x in enumerate(X)
                        if x % i == 0 or i % x == 0)
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))
