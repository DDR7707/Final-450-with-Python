#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		mini = arr[0]
		maxi = arr[0]
		
		final = arr[0]
		
		for i in range(1,n):
		    if arr[i] < 0:
		        mini , maxi = maxi , mini
		    
		    mini = min(arr[i] , mini*arr[i])
		    maxi = max(arr[i] , maxi*arr[i])
		    
		    final = max(maxi , final)
		    
    	return final 
