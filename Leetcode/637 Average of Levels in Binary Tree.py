# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while len(queue):
            curLevel = []
            for i in range(len(queue)):
                curNode = queue.pop(0)
                curLevel.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(float(sum(curLevel)) / len(curLevel))
        return res
