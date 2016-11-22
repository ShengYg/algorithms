# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.postorder(root ,nodes)
        return nodes
        
    def postorder(self, root, nodes):
        if not root:
            return
        self.postorder(root.left, nodes)
        self.postorder(root.right, nodes)
        nodes.append(root.val)
