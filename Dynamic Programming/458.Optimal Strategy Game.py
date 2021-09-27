def solve(arr , n):
    dp = [[0 for i in range(n)] for i in range(n)]

    for i in range(n-1):
        dp[i][i+1] = max(arr[i] , arr[i+1])
    
    for gap in range(3 , n , 2):
        for i in range(n-gap):
            j = i+gap
            dp[i][j] = max(arr[i] + min(dp[i+2][j] ,dp[i+1][j-1]) ,
                           arr[j] + min(dp[i][j-2] , dp[i+1][j-1]))
                           
    return dp
    

arr = [20, 30, 2, 2, 2, 10]
n = 6
print(solve(arr , n))
