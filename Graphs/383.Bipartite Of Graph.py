class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        look = {}
        if not dislikes:
            return True
        
        for i,j in dislikes:
            if j in look:
                look[j].append(i)
            else:
                look[j] = [i]
            if i in look:
                look[i].append(j)
            else:
                look[i] = [j]
        
        for i in range(1,n+1):
            if i not in look:
                look[i] = []
        
        color = [-1]*(n+1)
        def dfs(look , color , s , c):
            if color[s] != -1 and color[s] != c:
                return False
            
            color[s] = c
            ans = True
            for i in look[s]:
                if color[i] == -1:
                    ans &= dfs(look , color , i , 1-c)
                    
                if color[i] != -1 and color[i] == c:
                    return False
                
                if not ans:
                    return False
                
            return True       
        
        for k in look:
            if color[k] == -1:
                if dfs(look , color , k , 1) == False:
                    return False
        return True  
      
      
      
      
      
      
      
      
      
      
      
 class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        look = {}
        if not dislikes:
            return True
        
        for i,j in dislikes:
            if j in look:
                look[j].append(i)
            else:
                look[j] = [i]
            if i in look:
                look[i].append(j)
            else:
                look[i] = [j]
        
        for i in range(1,n+1):
            if i not in look:
                look[i] = []
        
        color = [-1]*n
        que = []
        for i in range(1,n+1):
            if color[i-1] == -1:
                que.append([i,0])
                color[i-1] = 0
                
                while que:
                    u = que[0][0]
                    c = que[0][1]
                    que.pop(0)
                    
                    for v in look[u]:
                        if color[v-1] == c:
                            return False
                        if color[v-1] == -1:
                            if c == 1:
                                color[v-1] = 0
                            else:
                                color[v-1] = 1
                            que.append([v,color[v-1]])    
        return True   
