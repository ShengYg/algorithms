# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.robsub(root, {})
    def robsub(self, root, nodemap):
        if not root:
            return 0
        if root in nodemap:
            return nodemap[root]
        val = 0
        if root.left:
            val += self.robsub(root.left.left, nodemap) + self.robsub(root.left.right, nodemap)
        if root.right:
            val += self.robsub(root.right.left, nodemap) + self.robsub(root.right.right, nodemap)
        val = max(val + root.val, self.robsub(root.left, nodemap) + self.robsub(root.right, nodemap))
        nodemap[root] = val
        return val
