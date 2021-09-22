def intersection(a, b, n, m):
 
    i = 0
    j = 0
 
    while (i < n and j < m):
 
        if (a[i] > b[j]):
            j += 1
 
        else:
            if (b[j] > a[i]):
                i += 1
 
            else:
                # when both are equal
                print(a[i], end=" ")
                i += 1
                j += 1
 
 
# Driver Code
if __name__ == "__main__":
 
    a = [1, 3, 2, 3, 4, 5, 5, 6]
    b = [3, 3, 5]
 
    n = len(a)
    m = len(b)
     
    # sort
    a.sort()
    b.sort()
     
    # function call
    intersection(a, b, n, m)
