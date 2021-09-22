class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        final = float("inf")
        i = 0
        j = M-1
        
        while j < N:
            final = min(final , A[j]-A[i])
            i += 1
            j += 1
        return final    
