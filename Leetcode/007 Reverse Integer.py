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

class Solution(object):
    def reverse(self, x):
        s = str(x)
        res = int(''.join(['-', s[1:][::-1]])) if s[0] == '-' else int(s[::-1])
        return res if -2147483648 <= res <= 2147483647 else 0
