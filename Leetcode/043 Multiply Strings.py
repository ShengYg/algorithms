class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        zero = ord('0')
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - zero) * (ord(num2[j]) - zero)
                p1, p2 = i + j, i + j + 1
                Sum = mul + pos[p2]
                pos[p1] += Sum / 10
                pos[p2] = Sum % 10
        result = 0
        for i in pos:
            result = result * 10 + i
        return str(result)
