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


from collections import defaultdict
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        required, min_len = defaultdict(int), sys.maxint
        
        for ch in t:
            required[ch] += 1
        start = min_start = 0
        min_end, count = -len(s) - 1, len(required)

        for i in xrange(len(s)):
            required[s[i]] -= 1
            if required[s[i]] == 0:
                if count == 1:
                    for j in xrange(start, i+1):
                        required[s[j]] += 1
                        if required[s[j]] > 0:
                            length = i - j
                            if length < min_len:
                                min_len = length
                                min_start, min_end = j, i
                            start = j + 1
                            break
                else:
                    count -= 1
        return s[min_start : min_end+1]


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        required, min_len = [0] * 256, 2147483647
        
        for ch in t:
            required[ord(ch)] += 1
        start = min_start = 0
        min_end, count = -len(s) - 1, len(required) - required.count(0)
        
        for i in xrange(len(s)):
            index = ord(s[i])
            required[index] -= 1
            if required[index] == 0:
                if count == 1:
                    for j in xrange(start, i+1):
                        index = ord(s[j])
                        required[index] += 1
                        if required[index] > 0:
                            length = i - j
                            if length < min_len:
                                min_len = length
                                min_start, min_end = j, i
                            start = j + 1
                            break
                else:
                    count -= 1
        return s[min_start : min_end+1]
