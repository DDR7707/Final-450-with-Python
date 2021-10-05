class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def convert(root):
    if not root:
        return 0
    
    left = convert(root.left)
    right = convert(root.right)
    
    temp = root.data + left + right
    root.data = left+right
    return temp

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data , end = " ")
        inorder(root.right)

root = newNode(10)
root.left = newNode(-2)
root.right = newNode(6)
root.left.left = newNode(8)
root.left.right = newNode(-4)
root.right.left = newNode(7)
root.right.right = newNode(5)

convert(root)
inorder(root)
