def krushals(graph , v):
    graph.sort(key = lambda x : x[2])
    parent = [i for i in range(v)]
    rank = [0 for i in range(v)]
    final = 0
    s = 0
    
    def find(x , parent):
        if x == parent[x]:
            return x
        return find(parent[x] , parent)
    
    def union(i , j , parent , rank):
        x = i #find(i , parent)
        y = j #fins(j , parent)
        
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        else:
            parent[x] = y
            rank[y] += 1
    
    for a,b,c in graph:
        if s > v-1:
            break
        
        x = find(a , parent)
        y = find(b , parent)
        if x != y:
            print(a,b,c)
            final += c
            union(x , y , parent , rank)
            s += 1
    print(parent , rank)
    return final


graph = [[0,1,4] ,
         [0,7,8] ,
         [1,2,8] ,
         [1,7,11] ,
         [2,3,7] ,
         [2,5,4] ,
         [2,8,2] ,
         [3,4,9] ,
         [3,5,14] ,
         [4,5,10] ,
         [5,6,2] ,
         [6,7,1] ,
         [6,8,6] ,
         [7,8,7]]
         
print(krushals(graph , 9))         
