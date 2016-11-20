# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = TreeNode(-float('inf'))
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.Traversal(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return
    
    ## recursive
    def Traversal(self, root):
        if not root:
            return
        self.Traversal(root.left)
        if not self.first and self.pre.val > root.val:
            self.first = self.pre
        if self.first and self.pre.val > root.val:
            self.second = root
        self.pre = root
        self.Traversal(root.right

    ## iterative
    def Traversal(self, root):
        toVisit = []
        curNode = root
        while curNode or len(toVisit) != 0:
            if curNode:
                toVisit.append(curNode)
                curNode = curNode.left
            else:
                curNode = toVisit.pop()
                if not self.first and self.pre.val > curNode.val:
                    self.first = self.pre
                if self.first and self.pre.val > curNode.val:
                    self.second = curNode
                self.pre = curNode
                curNode = curNode.right

    ## morris    
    def Traversal(self, root):
        curNode = root
        while curNode:
            if curNode.left:
                predecessor = curNode.left
                while predecessor.right and predecessor.right != curNode:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = curNode
                    curNode = curNode.left
                else:
                    predecessor.right = None
                    if not self.first and self.pre.val > curNode.val:
                        self.first = self.pre
                    if self.first and self.pre.val > curNode.val:
                        self.second = curNode
                    self.pre = curNode
                    curNode = curNode.right
            else:
                if not self.first and self.pre.val > curNode.val:
                    self.first = self.pre
                if self.first and self.pre.val > curNode.val:
                    self.second = curNode
                self.pre = curNode
                curNode = curNode.right
