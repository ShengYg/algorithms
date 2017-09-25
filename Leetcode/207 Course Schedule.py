class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for item in prerequisites:
            graph[item[0]].append(item[1])
        visited = [0] * numCourses
        # 0: no
        # 1: one time
        # 2: multi times
        for i in range(numCourses):
            if not visited[i]:
                ret = self.DFS_visit(visited, graph, i)
                if not ret:
                    return False
        return True
        
    def DFS_visit(self, visited, graph, i):
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                ret = self.DFS_visit(visited, graph, j)
                if not ret:
                    return False
            elif visited[j] == 1:
                return False
        visited[i] = -1
        return True
