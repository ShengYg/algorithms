from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
        

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = [0 for i in range(26)]
        for i in range(len(s)):
            count[ord(s[i]) - 97] += 1
        for i in range(len(t)):
            count[ord(t[i]) - 97] -= 1
        for item in count:
            if item:
                return False
        return True
