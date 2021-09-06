def reverseLevelOrder(root):
    # code here
    if not root:
        return root
    
    final = [root.data]
    que = [root]
    
    while que:
        temp = que.pop(0)
        
        if temp.right:
            final.insert(0,temp.right.data)
            que.append(temp.right)
        
        if temp.left:
            final.insert(0,temp.left.data)
            que.append(temp.left)
    
    return final  
