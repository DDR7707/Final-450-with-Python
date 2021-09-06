def solve(x,y,s1,s2):
        dp = [[0 for i in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        print(dp)           
        return dp[x][y] 


print(solve(3,2,"ABC" , "AC"))        
