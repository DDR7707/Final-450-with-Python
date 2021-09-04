class Solution:
    def sort012(self,arr,n):
        # code here
        l = 0
        m = 0
        r = n-1
        
        while m <= r:
            if arr[m] == 0:
                arr[m] , arr[l] = arr[l] , arr[m]
                l += 1
                m += 1
            
            elif arr[m] == 1:
                m += 1
            
            else:
                arr[r] , arr[m] = arr[m] , arr[r]
                r -= 1
                
        return arr 
