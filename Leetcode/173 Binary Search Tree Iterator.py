# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._stack = []
        while root:
            self._stack.append(root)
            root = root.left
                
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self._stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self._stack.pop()
        cur = node
        if cur.right:
            cur = cur.right
            self._stack.append(cur)
            while cur.left:
                cur = cur.left
                self._stack.append(cur)
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
