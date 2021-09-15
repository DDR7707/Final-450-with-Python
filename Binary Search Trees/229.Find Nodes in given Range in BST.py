def getCount(root,low,high):
    ##Your code here
    if not root:
        return 0
    
    
    if root.data >= low and root.data <= high:
        return 1 + getCount(root.left , low , high) + getCount(root.right , low , high)
    
    elif root.data < low:
        return getCount(root.right , low , high)
    
    return getCount(root.left , low , high)
