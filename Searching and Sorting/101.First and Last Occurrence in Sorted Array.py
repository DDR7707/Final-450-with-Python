def find(arr,n,x):
    # code here
    def binary1(arr , high , low , x , n):
        if high >= low:
            mid = (low + high) // 2
            if (mid == 0 or x > arr[mid-1]) and x == arr[mid]:
                return mid
            
            elif x > arr[mid]:
                return binary1(arr , high , mid+1 , x , n)
            else:
                return binary1(arr , mid-1 , low , x , n)
        else:
            return -1
    
    def binary2(arr , high , low , x , n):
        if high >= low:
            mid = (low + high) // 2
            if (mid == n-1 or x < arr[mid+1]) and x == arr[mid]:
                return mid
            
            elif x < arr[mid]:
                return binary2(arr , mid-1 , low , x , n)
            else:
                return binary2(arr , high , mid+1 , x , n)
        else:
            return -1
            
    r1 = binary1(arr , n-1 , 0 , x , n)
    r2 = binary2(arr , n-1 , 0 , x , n)
    
    return [r1 , r2]
  
  
  
  
  
  
# Other Approach


def first(arr, x, n):
     
    low = 0
    high = n - 1
    res = -1
     
    while (low <= high):
         
        # Normal Binary Search Logic
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the left
        # half.
        else:
            res = mid
            high = mid - 1
 
    return res
 
# If x is present in arr[] then returns
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1
def last(arr, x, n):
     
    low = 0
    high = n - 1
    res = -1
     
    while(low <= high):
         
        # Normal Binary Search Logic
        mid = (low + high) // 2
         
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
             
        # If arr[mid] is same as x, we
        # update res and move to the Right
        # half.
        else:
            res = mid
            low = mid + 1
 
    return res
 
# Driver code
arr = [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
n = len(arr)
x = 8
 
print("First Occurrence =", first(arr, x, n))
print("Last Occurrence =", last(arr, x, n))
