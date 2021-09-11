class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        final = []
        i = j = k = 0
        while i < n1 and j < n2 and k <n3:
            if A[i] == B[j] and B[j] == C[k]:
                final.append(A[i])
                i += 1
                j += 1
                k += 1
                continue
            
            if A[i] < B[j] and A[i] < C[k]:
                i += 1
            
            elif B[j] < A[i] and B[j] < C[k]:
                j += 1
            
            else:
                k += 1
        
        return final  
