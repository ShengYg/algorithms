class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = [int(a) for a in list(str(num))]
        for i in range(len(s)):
            ind, max = self.argmax(s[i+1:])
            ind = ind + i + 1
            if max > s[i]:
                s[i], s[ind] = s[ind], s[i]
                break
        return int(''.join([str(a) for a in s]))

    def argmax(self, num):
        max = 0
        ind = 0
        for i in range(len(num)):
            if num[i] >= max:
                max = num[i]
                ind = i
        return ind, max
