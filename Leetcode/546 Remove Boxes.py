class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        memo = [[[0] * 100 for _ in range(100)]for _ in range(100)]
        return self.dfs(boxes, memo, 0, n-1, 0)

    
    def dfs(self, boxes, memo, l, r, k):
        if l > r:
            return 0
        if memo[l][r][k]:
            return memo[l][r][k]
        while r > l and boxes[r] == boxes[r-1]:
            r -= 1
            k += 1
        memo[l][r][k] = self.dfs(boxes, memo, l, r-1, 0) + (k+1) * (k+1)
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                memo[l][r][k] = max(memo[l][r][k], self.dfs(boxes,memo,l,i,k+1) + self.dfs(boxes,memo,i+1,r-1,0))
        return memo[l][r][k]
