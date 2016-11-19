# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.inorder(root ,nodes)
        return nodes
        
    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)
