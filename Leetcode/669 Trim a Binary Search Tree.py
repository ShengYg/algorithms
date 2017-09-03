# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return self.dfs(root, L, R)

    def dfs(self, root, L, R):
        if not root:
            return
        if root.val < L:
            return self.dfs(root.right, L, R)
        elif root.val > R:
            return self.dfs(root.left, L, R)
        else:
            root.left = self.dfs(root.left, L, R)
            root.right = self.dfs(root.right, L, R)
            return root
        
