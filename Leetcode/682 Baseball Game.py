class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for item in ops:
            if item.isdigit() or item[1:].isdigit():
                stack.append(int(item))
            elif item == 'C':
                stack.pop()
            elif item == 'D':
                stack.append(stack[-1]*2)
            elif item == '+':
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
