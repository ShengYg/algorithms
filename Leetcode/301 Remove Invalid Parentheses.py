class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return ['']
        ans, pair = [], ['(', ')']
        self.remove(ans, s, 0, 0, pair)
        return ans

    def remove(self, ans, s, last_i, last_j, pair):
        index = 0
        for i in range(last_i, len(s)):
            if s[i] == pair[0]:
                index += 1
            if s[i] == pair[1]:
                index -= 1
            if index >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
                    self.remove(ans, s[0:j] + s[j + 1:len(s)], i, j, pair)
                    # ans.append(s[0:j] + s[j + 1:len(s)])
            return
        reverse_s = s[::-1]
        if pair[0] == '(':
            self.remove(ans, reverse_s, 0, 0, pair[::-1])
        else:
            ans.append(reverse_s)
