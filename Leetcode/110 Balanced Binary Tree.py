# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getDepth(root) != -1
    
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left != -1:
            right = self.getDepth(root.right)
            if right != -1:
                return 1 + max(left, right) if abs(left - right) <= 1 else -1
        return -1

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        try:
            return self.getDepth(root) != -1
        except:
            return False
    
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            raise Exception
        else:
            right = self.getDepth(root.right)
            if right == -1:
                raise Exception
            else:
                return 1 + max(left, right) if abs(left - right) <= 1 else -1
