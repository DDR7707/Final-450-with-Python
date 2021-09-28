def solve(arr , w):
    for i in arr:
        i.append(i[0] / i[1])
        
    arr.sort(key = lambda x : x[2])  
    final = 0
    
    while w > 0:
        if not arr:
            return final
            
        if arr[-1][1] == 0:
            arr.pop()
            continue
        
        if arr[-1][1] <= w:
            final += arr[-1][0]
            w -= arr[-1][1]
            arr.pop()
        
        else:
            final += arr[-1][2] * w
            w = 0
    return final        


arr = [[60,10] , [100,20]]
w = 50
print(solve(arr , w))
