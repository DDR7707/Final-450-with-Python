class Solution:
    def findPath(self, m, n):
        # code here
        def issafe(row,col,m,n,visited):
            if row == -1 or row == n or col == -1 or col == n or m[row][col] == 0 or visited[row][col]:
                return False
            return True
        
        def backtracking(row,col,m,n,path,final,visited):
            if row == -1 or row == n or col == -1 or col == n or m[row][col] == 0 or visited[row][col]:
                return
            
            if row == n-1 and col == n-1:
                final.append(path)
                return
            
            visited[row][col] = True
            
            if issafe(row+1,col,m,n,visited):
                path += "D"
                backtracking(row+1,col,m,n,path,final,visited)
                path = path[:-1]

            if issafe(row-1,col,m,n,visited):
                path += "U"
                backtracking(row-1,col,m,n,path,final,visited)
                path = path[:-1]

            if issafe(row,col+1,m,n,visited):
                path += "R"
                backtracking(row,col+1,m,n,path,final,visited)
                path = path[:-1]

            if issafe(row,col-1,m,n,visited):
                path += "L"
                backtracking(row,col-1,m,n,path,final,visited)
                path = path[:-1]   
            
            visited[row][col] = False
        
        
        final = []
        path = ""
        visited = [[0 for i in range(n)] for i in range(n)]
        
        backtracking(0,0,m,n,path,final,visited)
        
        final.sort()
        return final
