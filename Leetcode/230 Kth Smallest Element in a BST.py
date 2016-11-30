# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = self.count(root.left)
        if k <= cnt:
            return self.kthSmallest(root.left, k)
        elif k > cnt + 1:
            return self.kthSmallest(root.right, k - 1 - cnt)
        return root.val

    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        toVisit = []
        curNode = root
        while curNode or len(toVisit) != 0:
            if curNode:
                toVisit.append(curNode)
                curNode = curNode.left
            else:
                curNode = toVisit[-1]
                k -= 1
                if not k:
                    return curNode.val
                toVisit.pop()
                curNode = curNode.right
        return -1
