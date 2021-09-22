class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        final = 0
        look = set(arr)
        
        for i in range(N):
            if arr[i] - 1 not in look:
                j = arr[i]
                while j in look:
                    j += 1
                
                final = max(final , j-arr[i])
        return final   
