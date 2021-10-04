class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):

    cur = root
    stack = [] 
    final = []
    
    while True:
        if cur:
            final.append(cur.data)
            stack.append(cur)
            cur = cur.left
    
        elif stack:
            cur = stack.pop()
            cur = cur.right
        
        else:
            break
        
    return final
    
def rec_preorder(root):
    
    if root:
        print(root.data , end = " ")
        rec_preorder(root.left)
        rec_preorder(root.right)
    
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)
 
rec_preorder(root) 
print(preOrder(root))
