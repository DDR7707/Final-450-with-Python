def longestSubseqWithDiffOne(arr, n):
    # Initialize the dp[] array with 1 as a
    # single element will be of 1 length
    dp = [1 for i in range(n)]
 
    # Start traversing the given array
    for i in range(n):
        # Compare with all the previous elements
        for j in range(i):
            # If the element is consecutive then
            # consider this subsequence and update
            # dp[i] if required.
            if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1)):
                dp[i] = max(dp[i], dp[j]+1)
 
    # Longest length will be the maximum value
    # of dp array.
    result = 1  
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]
            
    return result
 
# Driver code
arr = [1, 2, 3, 4, 5, 3, 2]
# Longest subsequence with one difference is
# {1, 2, 3, 4, 3, 2}
n = len(arr)
print longestSubseqWithDiffOne(arr, n)




def longestSubsequence(A, N):
    L = [1]*N
    hm = {}
    for i in range(1,N):
        if abs(A[i]-A[i-1]) == 1:
            L[i] = 1 + L[i-1]
        elif hm.get(A[i]+1,0) or hm.get(A[i]-1,0):
            L[i] = 1+max(hm.get(A[i]+1,0), hm.get(A[i]-1,0))
        hm[A[i]] = L[i]
    return max(L)
# Driver code
A =  [1, 2, 3, 4, 5, 3, 2]
N = len(A)
print(longestSubsequence(A, N))
