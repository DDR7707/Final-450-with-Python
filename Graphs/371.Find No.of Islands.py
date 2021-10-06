def solve(grid):
	def bfs(grid , i , j):
	    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
	        return
	    grid[i][j] = 2
	    bfs(grid,i,j-1)
	    bfs(grid,i,j+1)
	    bfs(grid,i-1,j)
	    bfs(grid,i-1,j-1)
	    bfs(grid,i-1,j+1)
	    bfs(grid,i+1,j-1)
	    bfs(grid,i+1,j)
	    bfs(grid,i+1,j+1)
	    
	m = len(grid)
	n = len(grid[0])
	count = 0
	for i in range(m):
	    for j in range(n):
	        if grid[i][j] == 1:
	            count += 1
	            bfs(grid , i , j)
	return count 

graph = [[0,1],[1,0],[1,1],[1,0]]

print(solve(graph))






from collections import deque
 
# A function to check if a given cell
# (u, v) can be included in DFS
def isSafe(mat, i, j, vis):
     
    return ((i >= 0) and (i < 5) and 
            (j >= 0) and (j < 5) and
          (mat[i][j] and (not vis[i][j])))
 
def BFS(mat, vis, si, sj):
     
    # These arrays are used to get row and
    # column numbers of 8 neighbours of
    # a given cell
    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]
 
    # Simple BFS first step, we enqueue
    # source and mark it as visited
    q = deque()
    q.append([si, sj])
    vis[si][sj] = True
 
    # Next step of BFS. We take out
    # items one by one from queue and
    # enqueue their univisited adjacent
    while (len(q) > 0):
        temp = q.popleft()
 
        i = temp[0]
        j = temp[1]
 
        # Go through all 8 adjacent
        for k in range(8):
            if (isSafe(mat, i + row[k], j + col[k], vis)):
                vis[i + row[k]][j + col[k]] = True
                q.append([i + row[k], j + col[k]])
 
# This function returns number islands (connected
# components) in a graph. It simply works as
# BFS for disconnected graph and returns count
# of BFS calls.
def countIslands(mat):
      
    # Mark all cells as not visited
    vis = [[False for i in range(5)]
                  for i in range(5)]
    # memset(vis, 0, sizeof(vis));
 
    # 5all BFS for every unvisited vertex
    # Whenever we see an univisted vertex,
    # we increment res (number of islands)
    # also.
    res = 0
 
    for i in range(5):
        for j in range(5):
            if (mat[i][j] and not vis[i][j]):
                BFS(mat, vis, i, j)
                res += 1
 
    return res
 
# Driver code
if __name__ == '__main__':
     
    mat = [ [ 1, 1, 0, 0, 0 ],
            [ 0, 1, 0, 0, 1 ],
            [ 1, 0, 0, 1, 1 ],
            [ 0, 0, 0, 0, 0 ],
            [ 1, 0, 1, 0, 1 ]]
 
    print (countIslands(mat))
