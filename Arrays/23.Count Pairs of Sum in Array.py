class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        look = {}
        final = 0
        
        for i in range(n):
            if k - arr[i] in look:
                final += look[k-arr[i]]
            
            if arr[i] in look:
                look[arr[i]] += 1
            
            else:
                look[arr[i]] = 1
        
        return final  
