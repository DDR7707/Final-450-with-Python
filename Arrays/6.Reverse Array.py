def reverse(arr):
  return arr[::-1]

#or

def reverse(arr):
  l = 0
  r = len(arr) - 1
  
  while l < r:
    arr[l] , arr[r] = arr[r] , arr[l]
    l += 1
    r -= 1
  return arr

