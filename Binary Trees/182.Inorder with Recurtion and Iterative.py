class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):

    cur = root
    stack = [] 
    final = []
     
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
            
        elif stack :
            cur = stack.pop()
            final.append(cur.data)
            cur = cur.right
 
        else:
            break
        
    return final
    
def rec_inorder(root):
    
    if root:
        rec_inorder(root.left)
        print(root.data , end = " ")
        rec_inorder(root.right)
    
 
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print(inOrder(root))
rec_inorder(root)
