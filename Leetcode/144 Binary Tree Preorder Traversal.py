# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.preorder(root ,nodes)
        return nodes
        
    def preorder(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)
