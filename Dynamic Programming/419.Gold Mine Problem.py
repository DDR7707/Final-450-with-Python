def solve(arr , m , n):
    dp = [[0 for i in range(n)] for i in range(m)]
    
    for cols in range(n-1 , -1 , -1):
        for rows in range(m):
            if cols == n-1:
                right = 0
            else:
                right = dp[rows][cols+1]
            
            if cols == n-1 or rows == 0:
                right_up = 0
            else:
                right_up = dp[rows-1][cols+1]
            
            if cols == n-1 or rows == m-1:
                right_down = 0
            else:
                right_down = dp[rows+1][cols+1]
            
            dp[rows][cols] = arr[rows][cols] + max(right , right_up , right_down)    
    
    for i in dp:
        print(i , end = "\n")
    
    final = float("-inf")
    for i in range(m):
        final = max(final , dp[i][0])
    
    return final    

arr = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]
 
m = 4
n = 4

print(solve(arr , m , n))
