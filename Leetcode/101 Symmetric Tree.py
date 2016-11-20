# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.branch(root.left, root.right)
        
    def branch(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.branch(left.left, right.right) and self.branch(right.left, left.right)

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
    
        stack = []
        if root.left:
            if not root.right:
                return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right:
            return False
            
        while len(stack):
            if len(stack) % 2:
                return False
            right = stack.pop()
            left = stack.pop()
            if right.val != left.val:
                return False
            
            if left.left:
                if not right.right:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right:
                return False
            
            if left.right:
                if not right.left:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left:
                return False
    
        return True
