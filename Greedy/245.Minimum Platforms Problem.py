class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        final = 1
        maxi = 1
        while i < n and j < n:
            if arr[i] > dep[j]:
                j += 1
                maxi -= 1
            else:
                maxi += 1
                i += 1
            final = max(final , maxi)
        
        return final  
