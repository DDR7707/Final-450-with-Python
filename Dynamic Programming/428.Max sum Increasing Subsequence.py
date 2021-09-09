class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		final = Arr[:]
		for i in range(1,n):
		    for j in range(i):
		        if Arr[j] < Arr[i]:
		            final[i] = max(final[i] , final[j]+Arr[i])
		return max(final) 
