class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d)
        if not s or not d:
            return ''
        res, max_len = '', 0
        for d_i in d:
            if len(d_i) <= max_len:
                continue
            i, j, m, n = 0, 0, len(s), len(d_i)
            while i < m and j < n:
                if s[i] == d_i[j]:
                    j += 1
                i += 1
            if j == n and n > max_len:
                res = d_i
                max_len = n
        return res

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))
        if not s or not d:
            return ''
        for d_i in d:
            i, j, m, n = 0, 0, len(s), len(d_i)
            while i < m and j < n:
                if s[i] == d_i[j]:
                    j += 1
                i += 1
            if j == n :
                return d_i
        return ''

import heapq
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            word = heapq.heappop(heap)[1]
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ''
