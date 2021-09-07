def minmaxsum(arr , k):
    final = 0
    mini = []
    maxi = []
    
    for i in range(k):
        while mini and arr[mini[-1]] > arr[i]:
            mini.pop()
        
        while maxi and arr[maxi[-1] < arr[i]]:
            maxi.pop()
        
        mini.insert(0,i)
        maxi.insert(0,i)
    
        
    final += arr[mini[-1]] + arr[maxi[-1]]
    
    for i in range(k,len(arr)):
        
        while mini and mini[0] <= i-k:
            mini.pop(0)
        while maxi and maxi[0] <= i-k:
            maxi.pop(0)
            
        while mini and arr[mini[-1]] > arr[i]:
            mini.pop()
        while maxi and arr[maxi[-1]] < arr[i]:
            maxi.pop()
        
        
        mini.insert(0,i)
        maxi.insert(0,i)

        final += arr[mini[-1]] + arr[maxi[-1]]
    
    return final    
        
    pass


arr = [2,5,-1,7,-3,-1,-2]
print(minmaxsum(arr , 4))
