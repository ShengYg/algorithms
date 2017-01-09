class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret, smap = [], {}
        if len(words) < 2:
            return ret
        for i in range(len(words)):
            smap[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                str1 = words[i][0:j]
                str2 = words[i][j:]
                if self.ispalindrome(str1):
                    str2rev = str2[::-1]
                    if str2rev in smap and smap[str2rev] != i:
                        ret.append([smap[str2rev], i])
                if self.ispalindrome(str2):
                    str1rev = str1[::-1]
                    if str1rev in smap and smap[str1rev] != i and len(str2) !=0:
                        ret.append([i, smap[str1rev]])
        return ret
    
    def ispalindrome(self, s):
        return s == s[::-1]
