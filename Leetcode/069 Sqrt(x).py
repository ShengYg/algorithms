class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.sqx(x, 1, x)
    def sqx(self, x, s, e):
        if s > e:
            return e
        m = (s + e) / 2
        if x / m == m:
            return m
        elif x / m < m:
            return self.sqx(x, s, m - 1)
        else:
            return self.sqx(x, m + 1, e)


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        for i in range(15, -1, -1):
            n = 1 << i
            if (res + n) * (res + n) <= x:
                res += n
        return res
