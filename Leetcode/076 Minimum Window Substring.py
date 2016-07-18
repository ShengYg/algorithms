from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashtable, count = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            count -= hashtable[c] > 0
            hashtable[c] -= 1
            if not count:
                while hashtable[s[i]] < 0:
                    hashtable[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
