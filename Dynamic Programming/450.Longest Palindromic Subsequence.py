def solve(s , n):
    dp = [[1 for i in range(n)] for i in range(n)]
    for lg in range(2 , n+1):
        for i in range(n-lg+1):
            j = i+lg-1
            
            if s[i] == s[j] and lg == 2:
                dp[i][j] = 2 
            
            elif s[i] == s[j]:
                dp[i][j] = 2+dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j] , dp[i][j-1])
    
    for i in range(len(dp)):
        print(dp[i] , end = "\n")



s = "GEEKS FOR GEEKS"
n = len(s)
print(solve(s , n))
