class Solution(object):
    visited = None
    f_time = None
    time = None

    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for item in prerequisites:
            graph[item[1]].append(item[0])
        self.visited = [0] * numCourses
        self.time = 0
        self.f_time = [0] * numCourses
        for i in range(numCourses):
            if not self.visited[i]:
                try:
                    self.DFS_visit(graph, i)
                except:
                    return []
        ret = zip(self.f_time, range(numCourses))
        ret = sorted(ret, key=lambda x: x[0])[::-1]
        return [item[1] for item in ret]

    def DFS_visit(self, graph, i):
        self.time += 1
        self.visited[i] = 1
        for j in graph[i]:
            if not self.visited[j]:
                self.DFS_visit(graph, j)
            elif self.visited[j] == 1:
                raise
        self.visited[i] = -1
        self.time += 1
        self.f_time[i] = self.time
