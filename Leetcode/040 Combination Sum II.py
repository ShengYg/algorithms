class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.get_combination_sum(candidates, [], target, result)
        return result

    def get_combination_sum(self, candidates, cur, target, result):
        if sum(cur) == target:
            result.append(cur)
            return
        if sum(cur) > target:
            return

        ind = 0
        while ind < len(candidates):
            self.get_combination_sum(candidates[ind+1:], cur+[candidates[ind]], target, result)
            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]: 
                ind += 1
            ind += 1
