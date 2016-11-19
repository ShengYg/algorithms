# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes, toVisit = [], []
        curNode = root
        preNode = None
        while curNode or len(toVisit) != 0:
            if curNode:
                toVisit.append(curNode)
                curNode = curNode.left
            else:
                curNode = toVisit.pop()
                if preNode and curNode.val <= preNode.val:
                    return False
                preNode = curNode
                curNode = curNode.right
        return True
