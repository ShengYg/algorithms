class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        result = []
        self.get_combination(target, candidates, [], result)
        return result
        
    def get_combination(self, target, candidates, current, result):
        if not candidates or sum(current) > target:
            return
        if sum(current) == target:
            result.append(current)
            return
        for ind, val in enumerate(candidates):
            self.get_combination(target, candidates[ind:], current + [val], result)
