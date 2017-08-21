# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root.left and not root.right and not root.val:
            return False
        s = self.get_sum(root)
        if s % 2:
            return False
        self.res = False
        self.get_sum2(root, s / 2)
        return self.res

    def get_sum(self, root):
        if not root:
            return 0
        return root.val + self.get_sum(root.left) + self.get_sum(root.right)

    def get_sum2(self, root, val):
        if not root:
            return 0
        s = root.val + self.get_sum2(root.left, val) + self.get_sum2(root.right, val)
        if s == val:
            self.res = True
        return s
        
