class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        table = [[True for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    table[0][0] = True
                elif i == 0:
                    table[0][j] = table[0][j-1] and (s2[j-1] == s3[j-1])
                elif j == 0:
                    table[i][0] = table[i-1][0] and (s1[i-1] == s3[i-1])
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
        return table[-1][-1]
