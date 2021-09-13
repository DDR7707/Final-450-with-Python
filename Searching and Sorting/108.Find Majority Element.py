class Solution:
    def majorityElement(self, A, N):
        #Your code here
        look = A[0]
        c = 1
        
        for i in range(N):
            if A[i] == look:
                c += 1
            else:
                c -= 1
            if c == 0:
                look = A[i]
                c = 1
        
        final = 0
        for i in A:
            if i == look:
                final += 1
        
        return look if final > (N/2) else -1
