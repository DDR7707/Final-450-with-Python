def solve(arr , n):
    dp = [["" for i in range(n+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i-1] == arr[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + str(arr[i-1])
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp
    

arr = "axxxy"
n = len(arr)
print(solve(arr , n))
