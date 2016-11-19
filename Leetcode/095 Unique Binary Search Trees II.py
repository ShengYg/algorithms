class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTree(1, n)
    
    def genTree(self, start, end):
        list = []
        if start > end:
            list.append(None)
            return list
        if start == end:
            list.append(TreeNode(start))
            return list
        left, right = [], []
        for i in range(start, end + 1):
            left = self.genTree(start ,i - 1)
            right = self.genTree(i + 1, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right = rnode
                    list.append(root)
        return list
