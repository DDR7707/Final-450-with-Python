class Solution:
	def minJumps(self, arr, n):
	   # #code here
	   # maxi = n-1
	   # for i in range(n-2,-1,-1):
	   #     if i+arr[i] >= maxi:
	   #         maxi = i
	   # if maxi != 0:
	   #     return -1
	        
	        
	    l = 0
	    r = 0
	    c = 0
	    final = 0
	    
	    while r < n-1:
	        maxi = 0
	        for i in range(l , r+1):
	            maxi = max(maxi , i+arr[i])
	        if maxi == c:
	            return -1
	        c = maxi     
	        final += 1
	        l = r+1
	        r = maxi
	    return final      
	            
