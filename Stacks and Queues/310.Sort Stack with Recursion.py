def solve(arr):
    def rec(arr , ele):
        if not arr or arr[-1] < ele:
            arr.append(ele)
            return
        
        temp1 = arr.pop()
        rec(arr , ele)
        arr.append(temp1)
    
    if not arr:
        return
    
    temp = arr.pop()
    solve(arr)
    rec(arr , temp)
    return arr


arr = [-3,14,18,-5,30]
print(solve(arr))
