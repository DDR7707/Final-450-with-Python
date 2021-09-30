def addvertex(v):
    global graph
    if v not in graph:
        graph[v] = []

def addedge(v1 , v2):
    global graph
    if v1 in graph:
        graph[v1].append(v2)

def dfs(graph):
    def rec(graph , s , visited , p):
        visited[s] = 1
        for i in graph[s]:
            if visited[i] == False:
                return rec(graph , i , visited , s)
            elif i != p:
                return True
        return False        
        
    visited = [0]*len(graph)
    for i in graph:
        if visited[i] == False:
            if rec(graph , i , visited , -1) == True:
                return True
                
    return False            

def bfs(graph):
    visited = [0]*len(graph)
    parent = [-1]*len(graph)
    def rec(graph , visited , s , parent):
        que = []
        que.append(s)
        visited[s] = 1
        while que:
            temp = que.pop(0)
            for i in graph[temp]:
                if visited[i] == False:
                    visited[i] = True
                    que.append(i)
                    parent[i] = temp
                    
                elif i != parent[temp]:
                    return True
        return False
        
    for i in graph:
        if visited[i] == False:
            return rec(graph , visited , i , parent)
    return False    

graph1 = {0 : [1,2,3] ,
          1 : [0,2] ,
          2 : [0,1] ,
          3 : [0,4] ,
          4 : [3]
}

graph2 = {0 : [1],
          1 : [0,2] ,
          2 : [1]
}

print(bfs(graph1))
print(bfs(graph2))

print(dfs(graph1))
print(dfs(graph2))
