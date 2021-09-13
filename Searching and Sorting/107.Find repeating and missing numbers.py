def repeatedNumber(A):
     
    length = len(A)
    Sum_N = (length * (length + 1)) // 2
    Sum_NSq = ((length * (length + 1) *
                     (2 * length + 1)) // 6)
     
    missingNumber, repeating = 0, 0
     
    for i in range(len(A)):
        Sum_N -= A[i]
        Sum_NSq -= A[i] * A[i]
         
    missingNumber = (Sum_N + Sum_NSq //
                             Sum_N) // 2
    repeating = missingNumber - Sum_N
     
    ans = []
    ans.append(repeating)
    ans.append(missingNumber)
     
    return ans
 
# Driver code
v = [ 4, 3, 6, 2, 1, 6, 7 ]
res = repeatedNumber(v)
 
for i in res:
    print(i, end = " ")
