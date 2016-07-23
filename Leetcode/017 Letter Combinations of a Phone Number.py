class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: 
            return []
        ht = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = ['']
        for i in digits:
            tmp = []
            for s in res:
                for j in ht[i]:
                    tmp += [s + j]
            res = tmp
        return res
