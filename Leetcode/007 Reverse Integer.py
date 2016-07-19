class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while x:
            tail = x % 10
            result = result * 10 + tail
            x = x / 10
        result = 0 if abs(result) > 2147483647 else result
        return -result if neg else result
