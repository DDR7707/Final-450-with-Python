def merging_intervals(arr):
    arr.sort(key = lambda x : x[0])
    final = [arr[0]]
    print(arr)
    
    for a,b in arr[1:]:
        last = final[-1]
        if a <= last[1]:
            final[-1][1] = max(last[1] , b)
        else:
            final.append([a,b])
        print(final)    
    return final        

arr = [[1,3] , [2,6] , [8,10] , [15,18]]
print(merging_intervals(arr)) 
