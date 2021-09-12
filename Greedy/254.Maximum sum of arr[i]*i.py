class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        a.sort()
        final = 0
        for i in range(n):
            final += i*a[i]
        
        return final%(10**9+7)    
