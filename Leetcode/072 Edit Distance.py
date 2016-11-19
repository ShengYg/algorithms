class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        out = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            out[i][0] = i
        for j in range(1, n + 1):
            out[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    out[i][j] = out[i - 1][j - 1]
                    print out[i - 1][j - 1]
                else:
                    out[i][j] = min(out[i - 1][j - 1] + 1, out[i][j - 1] + 1, out[i - 1][j] + 1)
        return out[m][n]
