def maxSum(arr,n):
    # code here
    arr.sort()
    final = []
    l = 0
    r = len(arr)-1
    ans = 0
    
    while l < r:
        final.append(arr[l])
        final.append(arr[r])
        l += 1
        r -= 1
    
    if l == r:
        final.append(arr[l])
    
    for i in range(1,len(final)):
        ans += abs(final[i] - final[i-1])
    
    ans += abs(final[0] - final[-1])
    
    return ans
