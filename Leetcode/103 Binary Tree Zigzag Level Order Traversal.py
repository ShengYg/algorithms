# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## queue
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        lefttoright = True
        while len(queue):
            size = len(queue)
            curLevel = [0 for _ in range(size)]
            for i in range(size):
                curNode = queue.pop(0)
                index = i if lefttoright else size-i-1
                curLevel[index] = curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(curLevel)
            lefttoright = not lefttoright
        return res

## deque
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        lefttoright = True
        while len(queue):
            curLevel = []
            for i in range(len(queue)):
                if not lefttoright:
                    curNode = queue.popleft()
                    curLevel.append(curNode.val)
                    if curNode.right:
                        queue.append(curNode.right)
                    if curNode.left:
                        queue.append(curNode.left)
                else:
                    curNode = queue.pop()
                    curLevel.append(curNode.val)
                    if curNode.left:
                        queue.appendleft(curNode.left)
                    if curNode.right:
                        queue.appendleft(curNode.right)
                    
            res.append(curLevel)
            lefttoright = not lefttoright
        return res
