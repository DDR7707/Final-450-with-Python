def lcs(X, Y):
     
    # Find lengths of two strings
    m = len(X)
    n = len(Y)
 
    L = [[0 for i in range(n+1)] for j in range(2)]
 
    # Binary index, used to index current row and
    # previous row.
    bi = bool
     
    for i in range(m):
        # Compute current binary index
        bi = i&1
 
        for j in range(n+1):
            if (i == 0 or j == 0):
                L[bi][j] = 0
 
            elif (X[i] == Y[j - 1]):
                L[bi][j] = L[1 - bi][j - 1] + 1
 
            else:
                L[bi][j] = max(L[1 - bi][j],
                               L[bi][j - 1])
 
    # Last filled entry contains length of LCS
    # for X[0..n-1] and Y[0..m-1]
    return L[bi][n]
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
 
print("Length of LCS is", lcs(X, Y))
