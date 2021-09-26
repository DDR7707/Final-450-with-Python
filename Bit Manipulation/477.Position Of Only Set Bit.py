class Solution:
    def findPosition(self, N):
        # code here 
        if N == 0:
            return -1
        
        if N & (N-1) != 0:
            return -1
        
        def loop(n):
            if n > 1:
                return 1 + loop(n / 2)
            else:
                return 0
        
        return loop(N) + 1  
