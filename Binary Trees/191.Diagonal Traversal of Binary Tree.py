def diagonal(root):
    #:param root: root of the given tree.
    #return: print out the diagonal traversal,  no need to print new line
    #code here
    final = []
    que = []
    cur = root
    
    while cur:
        final.append(cur.data)
        
        if cur.left:
            que.append(cur.left)
        
        if cur.right:
            cur = cur.right
        else:
            if que:
                cur = que.pop(0)
            else:
                cur = None
    
    return final            
