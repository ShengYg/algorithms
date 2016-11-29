class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'\W|\s', '', s.lower())
        halflen = len(s)/2
        return s[:halflen] == s[-halflen:][::-1] if halflen >0 else True
