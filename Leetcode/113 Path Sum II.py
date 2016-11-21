# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result, curresult = [], []
        self.path(root, sum, result, curresult)
        return result

    def path(self, root, sum, result, curresult):
        if not root:
            return
        curresult.append(root.val)
        if root.val == sum and not root.left and not root.right:
            result.append(curresult[:])
            curresult.pop()
            return
        else:
            self.path(root.left, sum - root.val, result, curresult)
            self.path(root.right, sum - root.val, result, curresult)
        curresult.pop()
