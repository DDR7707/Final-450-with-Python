def solve(arr , n):
    arr1 = sorted(arr , key = lambda x:x[2] , reverse = True)
    final = [0 for i in range(n)]
    
    for a,b,c in arr1:
        i = b-1
        while i>=0:
            if final[i] == 0:
                final[i] = a
                break
            i -= 1
    ans = 0
    for i in final:
        if i != 0:
            ans += arr[i-1][2]
    
    return arr1 , final , ans
    pass



arr = [(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)]
arr1 = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
n = 5
n1 = 4
print(solve(arr , n))
