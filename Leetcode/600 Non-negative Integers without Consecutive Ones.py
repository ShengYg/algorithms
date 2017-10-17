class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:][::-1]
        n = len(num)
        a, b = [1]*n, [1]*n
        for i in range(1, n):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]
        res = a[n - 1] + b[n - 1]
        for i in range(n-2, -1, -1):
            if num[i] == '1' and num[i+1] == '1':
                break
            if num[i] == '0' and num[i+1] == '0':
                res -= b[i]
        return res

