class Graph:
    def __init__(self):
        self.graph = {}

    def addvertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def addegde(self, v, *u):
        if v in self.graph:
            for i in u:
                self.graph[v].append(i)

    def printgraph(self):
        print(self.graph)


def bfscycle(graph):
    count = 0
    look = [0] * len(graph)

    for i in graph:
        for j in graph[i]:
            look[j] += 1

    que = []
    for i in range(len(look)):
        if look[i] == 0:
            que.append(i)

    while que:
        temp = que.pop(0)
        for i in graph[temp]:
            look[i] -= 1
            if look[i] == 0:
                que.append(i)
        count += 1
    return count != len(graph)


def dfscycle(graph):
    visited = [0] * len(graph)
    stack = [0] * len(graph)

    def dfs(graph , visited , stack , i):
        visited[i] = 1
        stack[i] = 1
        for j in graph[i]:
            if visited[j] == 0:
                return dfs(graph , visited , stack , j)
            elif stack[j] == 1:
                return True
        stack[i] = 0
        return False            

    for i in graph:
        if visited[i] == 0:
            return dfs(graph, visited, stack, i)
    return False


graph = {0: [1, 2], 1: [2], 2: [0,3], 3: [3]}

print(bfscycle(graph))
print(dfscycle(graph))
