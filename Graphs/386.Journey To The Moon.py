def journeyToMoon(n, astronaut):
    # Write your code here
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    
    def find(x , parent):
        if x == parent[x]:
            return x
        return find(parent[x] , parent)
    
    def union(i , j , parent , rank):
        x = find(i , parent)
        y = find(j , parent)
        
        # This return step is optional
        if x == y:
            return
          
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
            
    for i,j in astronaut:      
        union(i,j,parent , rank) 
    # A*B + A*C + A*D + B*C + B*D + C*D = A*B + (A+B)*C + (A+B+C)*D
    final = [0 for i in range(n)]
    for i in parent:
        final[find(i,parent)] += 1
        
    ans = 0
    temp = 0
    for i in final:
        ans += i*temp
        temp += i
    return ans 
