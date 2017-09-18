class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = [0]
        for item in s:
            if item == '(':
                ret = [i+1 for i in ret]
            elif item == ')':
                ret = [i - 1 for i in ret]
                ret = filter(lambda x: x>=0, ret)
                if not ret:
                    return False
            else:
                mi = max(min(ret)-1, 0)
                ma = max(ret) + 1
                ret = range(mi, ma+1)
        return ret[0] == 0
