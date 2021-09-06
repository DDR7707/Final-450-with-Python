def weighted(arr):
    arr = sorted(arr , key = lambda x : x[1])
    final = [i[2] for i in arr]
    
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j][1] <= arr[i][0]:
                final[i] = max(final[i] , final[i]+final[j])
    
    return max(final)   
            
arr = [[3,10,20] , [1,2,50] , [6,19,100] , [2,100,200]]
print(weighted(arr))
