class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate("", result, n, n)
        return result
        
    def generate(self,subresult, result, l, r):
        if l > r:
            return
        if l > 0:
            self.generate(subresult + '(', result, l - 1, r)
        if r > 0:
            self.generate(subresult + ')', result, l, r - 1)
        if l == 0 and r == 0:
            result.append(subresult)
        return



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = [['']]
        for i in range(1, n + 1):
            result = []
            for j in range(i):
                for first in results[j]:
                    for second in results[i-1-j]:
                        result.append(''.join(['(', first, ')', second]))
            results.append(result)
        return results[len(results) - 1]

