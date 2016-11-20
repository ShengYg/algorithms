# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.branch(root.left, root.right)
        
    def branch(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.branch(left.left, right.right) and self.branch(right.left, left.right)
