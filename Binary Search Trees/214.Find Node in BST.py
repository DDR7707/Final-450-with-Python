# Search

def search(root,key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right,key)

    return search(root.left,key)
  
  
  # Insert
  def insert(root, Key):
    # code here
    if not root:
        return Node(Key)
    
    else:
        if root.data < Key:
            root.right = insert(root.right , Key)
        
        elif root.data > Key:
            root.left = insert(root.left , Key)
        
        else:
            return root
            
    return root        
