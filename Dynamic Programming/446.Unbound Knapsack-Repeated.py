def solve(wt , val , n , w):
    dp = [[0 for i in range(w+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            if j < wt[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j] , val[i-1]+dp[i][j - wt[i-1]])
    
    return dp[n][w]



wt = [1,3,4,5]
val = [1, 4, 5, 7]
n = 4
w = 8
print(solve(wt , val , n , w))
