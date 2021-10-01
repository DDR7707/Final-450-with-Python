class Graph:
    def __init__(self):
        self.graph = {}

    def addvertex(self,v):
        if v not in self.graph:
            self.graph[v] = []

    def addegde(self,v,*u):
        if v in self.graph:
            for i in u:
                self.graph[v].append(i)

    def printgraph(self):
        print(self.graph)

def khansalgo(graph):
    n = len(graph)
    zeros = [0]*n

    for i in graph:
        for j in graph[i]:
            zeros[j] += 1

    final = []
    que = []
    count = 0

    for i in range(len(zeros)):
        if zeros[i] == 0:
            que.append(i)

    while que:
        temp = que.pop(0)
        final.append(temp)
        count += 1
        for i in graph[temp]:
            zeros[i] -= 1
            if zeros[i] == 0:
                que.append(i)

    return final if count == len(graph) else -1           

def topodfs(graph):
    n = len(graph)
    stack = []
    visited = [0]*n

    def dfs(graph , stack , visited , s):
        visited[s] = 1
        for i in graph[s]:
            if visited[i] == 0:
                dfs(graph , stack , visited , i)
        stack.append(s)        


    for i in graph:
        if visited[i] == 0:
            dfs(graph , stack , visited , i)  
    return stack[::-1]        


g = Graph()
for i in range(5):
    g.addvertex(i)

g.addegde(0,1)
g.addegde(1,3)
g.addegde(2,3,4)
g.addegde(3,4)
g.printgraph()
print(khansalgo(g.graph))
print(topodfs(g.graph))
