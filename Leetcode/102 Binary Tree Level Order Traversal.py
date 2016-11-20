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

## BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while len(queue):
            curLevel = []
            for i in range(len(queue)):
                curNode = queue.pop(0)
                curLevel.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(curLevel)
        return res
