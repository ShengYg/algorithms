class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        s = ''
        rep = 0
        while len(s) < len(B):
            s += A
            rep += 1

        if s.find(B) >= 0:
            return rep
        s += A
        rep += 1
        if s.find(B) >= 0:
            return rep
        return -1
