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
                if len(st):
                    if s[st[-1]] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        if not len(st):
            longest = n
        else:
            a, b = n, 0
            while len(st):
                b = st[-1]
                st.pop()
                longest = max(longest, a - b - 1)
                a = b
            longest = max(longest, a)
        return longest
