class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_comp = 0
        max_so_far = arr[0]
        start = end = search = 0
        
        for i in range(N):
            max_comp = max_comp + arr[i]
            if max_comp > max_so_far:
                end = i
                start = search
                max_so_far = max_comp
            
            if max_comp < 0:
                search = search + 1
                max_comp = 0
        return max_so_far  
