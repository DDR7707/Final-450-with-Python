def count(S, m, n): 
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1

    
    for i in range(1 , m+1):
        for j in range(1 , n+1):
               dp[i][j] = dp[i-1][j] + dp[i][j - S[i-1]]
    
    return dp[m][n]         



S = [2,5,3,6]
m = 4
n = 10
print(count(S , m , n))
