class Solution(object):
### Method 1
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

### Method 2
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return 
    
            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])
        
        dfs(target, [])
        return result
