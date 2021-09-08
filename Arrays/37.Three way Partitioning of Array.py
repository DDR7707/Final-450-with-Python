class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    # code here 
	    low = 0
	    high = len(array)-1
	    mid = 0
	    
	    while mid <= high:
	        if array[mid] < a:
	            array[mid] , array[low] = array[low] , array[mid]
	            mid += 1
	            low += 1
	        elif array[mid] > b:
	            array[mid] , array[high] = array[high] , array[mid]
	            high -= 1
	        else:
	            mid += 1
	            
	    return array          
