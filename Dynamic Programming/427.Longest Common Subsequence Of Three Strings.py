def lcsOf3(X, Y, Z, m, n, o):
     
    L = [[[0 for i in range(o+1)] for j in range(n+1)]
         for k in range(m+1)]
 
    ''' Following steps build L[m+1][n+1][o+1] in
    bottom up fashion. Note that L[i][j][k]
    contains length of LCS of X[0..i-1] and
    Y[0..j-1] and Z[0.....k-1] '''
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                     
                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]):
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
 
                else:
                    L[i][j][k] = max(max(L[i-1][j][k],
                    L[i][j-1][k]),
                                    L[i][j][k-1])
 
    # L[m][n][o] contains length of LCS for
    # X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]
 
# Driver program to test above function
 
X = 'AGGT12'
Y = '12TXAYB'
Z = '12XBA'
 
m = len(X)
n = len(Y)
o = len(Z)
 
print('Length of LCS is', lcsOf3(X, Y, Z, m, n, o))








def solve(arr1 , arr2 , n1 , n2):
    dp = [["" for i in range(n2+1)] for i in range(n1+1)]
    
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + str(arr1[i-1])
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[i][j]
    

arr1 = "AGGT12"
arr2 = "12TXAYB"
arr3 = "12XBA"
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)
m = solve(arr1 , arr2 , n1 , n2)
print(solve(m , arr3 , len(m) , n3))
