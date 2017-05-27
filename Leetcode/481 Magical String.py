class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        a = [0] * (n+1)
        a[:3] = [1, 2, 2]
        head, tail, num, res = 2, 3, 1, 1
        while tail < n:
            i = 0
            while i < a[head]:
                a[tail] = num
                if num == 1 and tail < n:
                    res += 1
                tail += 1
                i += 1
            num ^= 3
            head += 1
        return res

