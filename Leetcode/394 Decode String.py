class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, idx = '', 0
        countStack, resStack = [], []
        while idx < len(s):
            if s[idx].isdigit():
                count = 0
                while s[idx].isdigit():
                    count = 10 * count + int(s[idx])
                    idx += 1
                countStack.append(count)
            elif s[idx] == '[':
                resStack.append(res)
                res = ''
                idx += 1
            elif s[idx] == ']':
                repeatTimes = countStack.pop()
                res = res * repeatTimes
                res = resStack.pop() + res
                idx += 1
            else:
                res += s[idx]
                idx += 1
        resStack.append(res)
        return ''.join(resStack)
