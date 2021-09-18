class Solution:
    def countFriendsPairings(self, n):
        # code here 
        a = 0
        b = 1
        c = 2
        if n <= 2:
            return n
            
        for i in range(3 , n+1):
            temp = c
            c = c + (i-1)*b
            a = b
            b = temp
        
        return c%(10**9+7) 
