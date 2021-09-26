class Solution:
	def setBits(self, N):
		# code here
		final = 0
		while N:
		     N = N & (N-1)
		     final += 1
		return final   
