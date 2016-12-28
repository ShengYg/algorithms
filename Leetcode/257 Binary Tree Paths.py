# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        answer = []
        if root:
            self.dfs(root, "", answer)
        return answer
        
    def dfs(self, root, path, answer):
        if not root.left and not root.right:
            answer.append(path + str(root.val))
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->", answer)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", answer)
