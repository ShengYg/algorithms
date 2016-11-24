# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h = self.height(root)
        if h == 1:
            return 1
        rheight = self.height(root.right)
        if rheight == h - 1:
            return pow(2, h - 1) + self.countNodes(root.right)
        else:
            return pow(2, h - 2) + self.countNodes(root.left)
        
    def height(self, root):
        h = 0
        while root:
            root = root.left
            h += 1
        return h
