class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        dp = [[0 for i in range(y)] for i in range(x)]
        
        for i in range(1,x):
            for j in range(1,y):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
                    
        return dp[x-1][y-1] 
