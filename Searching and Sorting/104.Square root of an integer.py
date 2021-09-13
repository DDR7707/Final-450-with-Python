def floorSqrt(x) :
  
    # Base cases
    if (x == 0 or x == 1) :
        return x
   
    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x   
    while (start <= end) :
        mid = (start + end) // 2
          
        # If x is a perfect square
        if (mid*mid == x) :
            return mid
              
        # Since we need floor, we update 
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid < x) :
            start = mid + 1
            ans = mid
              
        else :
              
            # If mid*mid is greater than x
            end = mid-1
              
    return ans
  
# driver code    
x = 11
print(floorSqrt(x))



# Other Approach


# python3 program for Babylonian
# method for square root
 
# Returns the square root of n.
# Note that the function
# will not work for numbers
# which are not perfect squares
 
def squareRoot(n):
    x = n;
    y = 1;
    while(x > y):
        x = (x + y) / 2;
        y = n / x;
    return x;
 
# Driver Code
n = 49;
print("root of", n, "is", squareRoot(n));
