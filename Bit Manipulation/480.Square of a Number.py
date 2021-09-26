def square(n):
 
    # Base case
    if (n == 0):
        return 0
 
    # Handle negative number
    if (n < 0):
        n = -n
 
    # Get floor(n/2) using
    # right shift
    x = n >> 1
 
    # If n is odd
    if (n & 1):
        return ((square(x) << 2)
                + (x << 2) + 1)
 
    # If n is even
    else:
        return (square(x) << 2)
 
 
# Driver Code
for n in range(1, 6):
    print("n = ", n, " n^2 = ",
          square(n))
