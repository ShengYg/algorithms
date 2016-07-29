class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, longest, st = len(s), 0, []
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if st:
                    if s[st[-1]] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        if not st:
            longest = n
        else:
            a, b = n, 0
            while st:
                b = st[-1]
                st.pop()
                longest = max(longest, a - b - 1)
                a = b
            longest = max(longest, a)
        return longest



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0
        curMax, longest = 0, [0]*n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    longest[i] = longest[i-2] + 2 if i >= 2 else 2
                    curMax = max(longest[i], curMax)
                else:
                    if i-longest[i-1]-1 >= 0 and s[i-longest[i-1]-1] == '(':
                        longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1]-2] \
                        if i-longest[i-1]-2 >= 0 else 0)
                        curMax = max(longest[i],curMax)
        return curMax



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0
        curMax, longest = 0, [0]*n
        for i in range(1, n):
            if s[i] == ')' and i-longest[i-1]-1 >= 0 and s[i-longest[i-1]-1] == '(':
                longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1]-2] \
                if i-longest[i-1]-2 >= 0 else 0)
                curMax = max(longest[i],curMax)
        return curMax
