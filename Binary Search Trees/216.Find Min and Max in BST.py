def minValue(root):
    ##Your code here
    cur = root
    while cur.left:
        cur = cur.left
    mini  = cur.data
    cur = root
    while cur.right:
      cur = cur.right
    maxi = cur.data  
    return mini , maxi 
