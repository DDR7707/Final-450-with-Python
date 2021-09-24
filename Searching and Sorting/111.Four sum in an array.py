def find4Numbers(A, n, X):
 
    # Sort the array in increasing order,
    # using library function for quick sort
    A.sort()
 
    # Now fix the first 2 elements one by
    # one and find the other two elements
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
             
            # Initialize two variables as indexes
            # of the first and last elements in
            # the remaining elements
            l = j + 1
            r = n - 1
 
            # To find the remaining two elements,
            # move the index variables (l & r)
            # toward each other.
            while (l < r):
                if(A[i] + A[j] + A[l] + A[r] == X):
                    print(A[i], ",", A[j], ",",
                          A[l], ",", A[r])
                    l += 1
                    r -= 1
                 
                elif (A[i] + A[j] + A[l] + A[r] < X):
                    l += 1
                else: # A[i] + A[j] + A[l] + A[r] > X
                    r -= 1
 
# Driver Code
if __name__ == "__main__":
     
    A = [1, 4, 45, 6, 10, 12]
    X = 21
    n = len(A)
    find4Numbers(A, n, X)
