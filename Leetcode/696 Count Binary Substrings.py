class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        one, zero = 0, 0
        ret = 0
        if s[0] == '0':
            zero = 1
        else:
            one = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1':
                    ret += min(one, zero)
                    zero = 1
                else:
                    zero += 1
            else:
                if s[i-1] == '0':
                    ret += min(one, zero)
                    one = 1
                else:
                    one += 1
        ret += min(one, zero)
        return ret
