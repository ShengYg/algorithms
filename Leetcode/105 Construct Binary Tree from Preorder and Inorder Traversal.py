# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.recursive(0, 0, len(preorder) - 1, preorder, inorder)
        
    def recursive(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        inIndex = inorder.index(root.val)
        root.left = self.recursive(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        root.right = self.recursive(preStart + inIndex + 1 - inStart, inIndex + 1, inEnd, preorder, inorder)
        return root
