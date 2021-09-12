def findMinDiff(A,N,M):
        A.sort()
        final = float("inf")
        i = 0
        j = M-1
        while j < N:
            final = min(final , A[j]-A[i])
            i += 1
            j += 1
        return final

print(findMinDiff([12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50] , 17 , 7))        
