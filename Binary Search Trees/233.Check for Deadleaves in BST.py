def isdeadEnd(root):
    # Code here
    def fun(root , mini , maxi):
        if not root:
            return False
        
        if mini == maxi:
            return True
        
        return fun(root.left , mini , root.data-1) or fun(root.right , root.data + 1 , maxi)
    
    return fun(root , 1 , float("inf"))    
