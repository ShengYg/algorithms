# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.help(root)
        if res == float('inf'):
            return -1
        return res

    def help(self, root):
        if not root.left:
            return float('inf')
        if root.left.val < root.right.val:
            return min(self.help(root.left), root.right.val)
        elif root.left.val > root.right.val:
            return min(self.help(root.right), root.left.val)
        else:
            return min(self.help(root.right), self.help(root.left))
