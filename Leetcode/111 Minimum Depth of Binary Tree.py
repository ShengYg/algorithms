# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.path(root)
        
    def path(self, root):
        if not root:
            return float('inf')
        left = self.path(root.left)
        right = self.path(root.right)
        if left == float('inf') and right == float('inf'):
            return 1
        return min(left, right) + 1
