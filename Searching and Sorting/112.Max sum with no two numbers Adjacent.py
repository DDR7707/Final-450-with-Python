class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0] , a[1])
        
        i = a[0]
        j = max(a[0] , a[1])
        final = 0
        
        for k in range(2 , n):
            final = max(a[k]+i , j)
            i = j
            j = final
        
        return final  
