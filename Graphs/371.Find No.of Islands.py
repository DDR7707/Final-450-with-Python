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
