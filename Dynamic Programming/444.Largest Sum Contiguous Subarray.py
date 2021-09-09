class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_comp = 0
        max_far = arr[0]
        
        for i in range(N):
            max_comp += arr[i]
            if max_comp > max_far:
                max_far = max_comp
            if max_comp < 0:
                max_comp = 0
        return max_far

    
def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far    
