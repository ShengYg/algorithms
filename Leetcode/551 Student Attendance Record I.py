class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for i in s:
            if i == 'A':
                a += 1
                l = 0
                if a > 1:
                    return False
            elif i == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
        return True
