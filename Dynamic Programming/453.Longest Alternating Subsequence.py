def LAS(arr, n):
   
    # "inc" and "dec" initialized as 1
    # as single element is still LAS
    inc = 1
    dec = 1
     
    # Iterate from second element
    for i in range(1,n):
       
        if (arr[i] > arr[i-1]):
           
            # "inc" changes iff "dec"
            # changes
            inc = dec + 1
        elif (arr[i] < arr[i-1]):
           
            # "dec" changes iff "inc"
            # changes
            dec = inc + 1
             
    # Return the maximum length
    return max(inc, dec)
 
# Driver Code
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 49, 50, 31, 60]
    n = len(arr)
     
    # Function Call
    print(LAS(arr, n))
