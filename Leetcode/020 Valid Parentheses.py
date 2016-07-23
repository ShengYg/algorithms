class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        buff = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                buff.append(i)
            elif i == ')' and len(buff) and buff.pop() == '(':
                continue
            elif i == ']' and len(buff) and buff.pop() == '[':
                continue
            elif i == '}' and len(buff) and buff.pop() == '{':
                continue
            else:
                return False
        if buff:
            return False
        return True
