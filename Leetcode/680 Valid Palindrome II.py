class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        length = len(s)
        flag = False
        for i in range(length/2):
            j = length-i-1
            if s[i] != s[j]:
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])
        return True

    def isPalindrome(self, s):
        return s == s[::-1]
