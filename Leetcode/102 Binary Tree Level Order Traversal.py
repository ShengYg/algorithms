## recursive
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.recursive(res, root ,0)
        return res
        
    def recursive(self, res, root, level):
        if not root:
            return
        if len(res) <= level:
            cur = []
            cur.append(root.val)
            res.append(cur)
        else:
            cur = res[level]
            cur.append(root.val)
        self.recursive(res, root.left, level + 1)
        self.recursive(res, root.right, level + 1)


