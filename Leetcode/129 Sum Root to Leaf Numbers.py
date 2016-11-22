# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.path(root, 0)
    def path(self, root, sum):
        if not root:
            return 0
        if not root.left and not root.right:
            return sum * 10 + root.val
        return self.path(root.left, sum * 10 + root.val) + self.path(root.right, sum * 10 + root.val)
