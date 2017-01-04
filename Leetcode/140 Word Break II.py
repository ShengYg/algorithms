class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.DFS(s, wordDict, {})
        
    def DFS(self, s, wordDict, strmap):
        if s in strmap:
            return strmap[s]
        res = []
        if not len(s):
            res.append('')
            return res
        for word in wordDict:
            if s.startswith(word):
                sublist = self.DFS(s[len(word):], wordDict, strmap)
                for sub in sublist:
                    res.append(word + (' ' if len(sub) else '') + sub)
        strmap[s] = res
        return res
