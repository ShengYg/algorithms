# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -float('inf')
        self.path(root)
        return self.maxValue
    
    def path(self, root):
        if not root:
            return 0
        left = max(0, self.path(root.left))
        right = max(0, self.path(root.right))
        self.maxValue = max(self.maxValue, left + right + root.val)
        return max(left, right) + root.val
