from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        n, cnt = len(s), len(words)
        if n <= 0 or cnt <= 0:
            return []
        d = defaultdict(int)
        for i in range(cnt):
            d[words[i]] += 1
        
        wl = len(words[0])
        for i in range(wl):
            left, count = i, 0
            td = defaultdict(int)
            for j in range(i, n-wl+1, wl):
                string = s[j:j+wl]
                if d[string]:
                    td[string] += 1
                    if td[string] <= d[string]:
                        count += 1
                    else:
                        while td[string] > d[string]:
                            str1 = s[left:left+wl]
                            td[str1] -= 1
                            if td[str1] < d[str1]:
                                count -= 1
                            left += wl
                    if count == cnt:
                        res.append(left)
                        td[s[left:left+wl]] -= 1
                        count -= 1
                        left += wl
                else:
                    td = defaultdict(int)
                    count = 0
                    left = j + wl
        return res
