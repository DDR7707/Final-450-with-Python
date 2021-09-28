class Solution:
	def LongestRepeatingSubsequence(self, str):
		# Code here
		dp = [[0 for i in range(len(str)+1)] for i in range(len(str)+1)]
		
		for i in range(1,len(str)+1):
		    for j in range(1,len(str)+1):
		        if str[i-1] == str[j-1] and i != j:
		            dp[i][j] = dp[i-1][j-1] + 1
		        else:
		            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
		return dp[i][j]
