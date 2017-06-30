class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLen, start = 1, 0
        for i in range(1, len(s)):
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        maxRight, pos = 0, 0
        RL = [0] * len(s)
        for i in range(len(s)):
	    if i < maxRight:
	        RL[i] = min(RL[2 * pos - i], maxRight - i)
	    else:
	        RL[i] = 1
	    while i >= RL[i] and i + RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
	        RL[i] += 1
	    if i + RL[i] - 1 > maxRight:
	        maxRight = i + RL[i] - 1
	        pos = i
        return ''.join(s[2*pos-maxRight:maxRight+1].split('#')) 
