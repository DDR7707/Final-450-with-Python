def solve(arr , k):
    if not arr:
        arr.append(k)
        return
    m = arr.pop()
    solve(arr , k)
    arr.append(m)
    
    return arr
    
        
    pass


arr = [2,3,4,5]
print(solve(arr , 1))
