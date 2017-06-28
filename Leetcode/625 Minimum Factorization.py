class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a
        res = []
        for i in range(9, 1, -1):
            while a % i == 0:
                a = a / i
                res.append(i)
        if a != 1:
            return 0
        result = 0
        for item in res[::-1]:
            result = result * 10 + item
        return result if result <= 2147483647 else 0
