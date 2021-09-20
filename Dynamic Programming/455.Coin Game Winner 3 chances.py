def solve(n , x , y):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    
    for i in range(2,n+1):
        if not dp[i-1]:
            dp[i] = 1
        elif i - x >= 0 and not dp[i-x]:
            dp[i] = 1
        elif i - y >= 0 and not dp[i-y]:
            dp[i] = 1
        else:
            dp[i] = 0
    
    return dp      

n = 5
x = 3
y = 4
print(solve(n , x , y))
