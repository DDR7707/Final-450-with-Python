def bridge(graph):
    time = 1
    visited = [0]*len(graph)
    parent = [-1]*len(graph)
    disc = [float("Inf")]*len(graph)
    low = [float("Inf")]*len(graph)
    
    def dfs(graph , u):
        nonlocal time , visited , parent , disc , low
        visited[u] = 1
        disc[u] = time
        low[u] = time
        time += 1
        
        for v in graph[u]:
            if visited[v] == 0:
                parent[v] = u
                dfs(graph , v)
                
                low[u] = min(low[u] , low[v])
                
                if low[v] > disc[u]:
                    print((u,v))
            
            elif v != parent[u]:
                low[u] = min(low[u] , disc[v])
                
    
    for i in graph:
        if visited[i] == 0:
            dfs(graph , i)
    
    return disc , low , time        


graph = {0 : [1,2] , 
        1 : [0,2,3,4,6] ,
        2 : [0,1] ,
        3 : [1,5] ,
        4 : [1,5] ,
        5 : [3,4] ,
        6 : [1]
}
print(bridge(graph))
