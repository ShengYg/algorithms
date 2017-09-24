class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = range(3000)
        for i in range(len(edges)):
            x = edges[i][0]
            y = edges[i][1]
            if p[x] == p[y]:
                return edges[i]
            tmp = p[y]
            for j in range(3000):
                if p[j] == tmp:
                    p[j] = p[x]
        return
