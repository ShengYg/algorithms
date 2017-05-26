class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        maxLength = None
        count = [0]*26
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25):
                maxLength += 1
            else:
                maxLength = 1
            count[ord(p[i])-97] = max(count[ord(p[i])-97], maxLength)
        return sum(count)
