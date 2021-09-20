def solve(arr , n , num):
    arr.sort()
    ans = float("inf")
    def floor(sam , k):
        low = 0
        high = len(sam)-1
        final = 0
        while low <= high:
            mid = (low+high) // 2
            if sam[mid] > k:
                high = mid-1
            
            else:
                final = mid
                low = mid+1
        return final
    
    for i in range(n):
        temp = arr[i+1:]
        ind = floor(temp , num+arr[i])
        ans = min(ans , i+(len(temp)-ind-1))
        
        print(num+arr[i] , ind , i+(len(temp)-ind-1) , ans)

    return ans    

arr = [1, 3, 4, 9, 10, 11, 12, 17, 20]
n = len(arr) 
num = 4
print(solve(arr , n , num))
