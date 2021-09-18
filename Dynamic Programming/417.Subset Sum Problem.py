def isPossible(elements, target):
 
    dp = [False]*(target+1)
 
    # initializing with 1 as sum 0 is always possible
    dp[0] = True
 
    # loop to go through every element of the elements array
    for ele in elements:
       
        # to change the value o all possible sum values to True
        for j in range(target, ele - 1, -1):
            if dp[j - ele]:
                dp[j] = True
 
    # If target is possible return True else False
    return dp[target]
 
# Driver code
arr = [6, 2, 5]
target = 7
 
if isPossible(arr, target):
    print("YES")
else:
    print("NO")
