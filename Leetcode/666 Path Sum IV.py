from collections import defaultdict
class Solution(object):
    tree = defaultdict()
    s = 0
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in nums:
            key = item / 10
            value = item % 10
            self.tree[key] = value
        if 11 not in self.tree:
            return 0
        self.path(11, [])
        return self.s

    def path(self, root, curresult):
        i = root / 10
        j = root % 10
        left = (i + 1) * 10 + 2 * j - 1
        right = (i + 1) * 10 + 2 * j
        curresult.append(self.tree[root])
        if not left in self.tree and not right in self.tree:
            self.s += sum(curresult)
            curresult.pop()
            return
        else:
            if left in self.tree:
                self.path(left, curresult)
            if right in self.tree:
                self.path(right, curresult)
        curresult.pop()
