class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		final = []
		for i in range(n):
		    if arr[i] == i+1:
		        final.append(i+1)
		return final   
