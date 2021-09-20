def solve(arr , n):
    res = sum(arr)
    
    if res % 2 == 0:
        res //= 2
    else:
        return 0
        
    dp = [0 for i in range(res+1)]
    dp[0] = 1
    
    for i in arr:
        for j in range(res , i-1 , -1):
            if dp[j - i] == 1:
                dp[j] = 1
            else:
                continue
    print(dp)
    return 1 if dp[res] == 1 else 0     
    pass

arr = [1,5,11,5]
n = 4
print(solve(arr , n))
