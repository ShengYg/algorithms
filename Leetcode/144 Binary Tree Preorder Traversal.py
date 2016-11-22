# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        self.preorder(root ,nodes)
        return nodes
        
    def preorder(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes, toVisit = [], []
        curNode = root
        while curNode or len(toVisit) != 0:
            if curNode:
                nodes.append(curNode.val)
                toVisit.append(curNode)
                curNode = curNode.left
            else:
                curNode = toVisit.pop()
                curNode = curNode.right
        return nodes

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes, toVisit = [], []
        curNode = root
        while curNode:
            if curNode.left:
                predecessor = curNode.left
                while predecessor.right and predecessor.right != curNode:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = curNode
                    nodes.append(curNode.val)
                    curNode = curNode.left
                else:
                    predecessor.right = None
                    curNode = curNode.right
            else:
                nodes.append(curNode.val)
                curNode = curNode.right
        return nodes
