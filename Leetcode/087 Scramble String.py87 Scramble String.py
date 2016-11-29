import collections
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if collections.Counter(s1) != collections.Counter(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]):
                return True
        return False

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        s3 = s2[::-1]
        if s1 == s2 or s1 == s3:
            return True
        count1, count2, count3 = [0]*26, [0]*26, [0]*26
        index = lambda x:ord(x)-97
        for i in range(1, len(s1)):
            count1[index(s1[i-1])] += 1
            count2[index(s2[i-1])] += 1
            count3[index(s3[i-1])] += 1
            if count1 == count2 and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if count1 == count3 and self.isScramble(s1[:i], s3[:i]) and self.isScramble(s1[i:], s3[i:]):
                return True
        return False
