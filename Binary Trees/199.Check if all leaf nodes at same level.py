class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def check(root):
    final = 0
    temp = 0
    
    def rec(root , level):
        nonlocal final
        if not root:
            return True
        
        if root.left == None and root.right == None:
            if final == 0:
                final = level
                return True
            
            return level == final
        
        return rec(root.left , level+1) and rec(root.right , level+1)    
        
            
    
    return rec(root , temp)

root = Node(12)
root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.left.left = Node(1)
root.left.right.left = Node(2)

print(check(root))
