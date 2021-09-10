def solve(arr, n):
 
    # sort the array
    arr.sort()
 
    # let two numbers be a and b
    a = 0; b = 0
    for i in range(n):
     
        # Fill a and b with every alternate
        # digit of input array
        if (i % 2 != 0):
            a = a * 10 + arr[i]
        else:
            b = b * 10 + arr[i]
 
    # return the sum
    return a + b
 
# Driver code
arr = [6, 8, 4, 5, 2, 3]
n = len(arr)
print("Sum is ", solve(arr, n))
