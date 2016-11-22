# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue, out = deque([root]), []
        while len(queue):
            out.append(queue[0].val)
            for i in range(len(queue)):
                curNode = queue.popleft()
                if curNode.right:
                    queue.append(curNode.right)
                if curNode.left:
                    queue.append(curNode.left)
        return out
