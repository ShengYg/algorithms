class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = a.split('+')
        a1 = int(a1)
        a2 = -int(a2[1:-1]) if a2[0] == '-' else int(a2[:-1])
        b1, b2 = b.split('+')
        b1 = int(b1)
        b2 = -int(b2[1:-1]) if b2[0] == '-' else int(b2[:-1])
        return str(a1*b1-a2*b2) + '+' + str(a1*b2 + a2*b1) + 'i'
