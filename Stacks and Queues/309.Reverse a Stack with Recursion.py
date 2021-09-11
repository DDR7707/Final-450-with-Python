def solve(arr):
    
    def insert(arr , temp):
        if not arr:
            arr.append(temp)
        else:
            temp1 = arr.pop()
            insert(arr , temp)
            arr.append(temp1)
        
        
    if not arr:
        return 
    temp = arr.pop()
    solve(arr)
    insert(arr , temp)
    return arr


arr = [1,2,3,4]
print(solve(arr))
