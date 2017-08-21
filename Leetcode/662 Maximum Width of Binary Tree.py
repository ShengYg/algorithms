# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        queue.append((root, 0))
        res = 0
        while len(queue):
            curLevel = []
            for i in range(len(queue)):
                curNode, width = queue.pop(0)
                curLevel.append(width)
                if curNode.left:
                    queue.append((curNode.left, 2*width))
                if curNode.right:
                    queue.append((curNode.right, 2*width+1))
            res = max(curLevel[-1] - curLevel[0] + 1, res)
        return res
