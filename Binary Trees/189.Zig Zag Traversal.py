# Binary Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to print the zigzag traversal
def zigZagTraversal(root):
    q = deque([])
    v = []
    q.append(root)
    v.append(root.data)
   
    # set initial level as 1, because root is
    # already been taken care of.
    l = 1
                
    while len(q) > 0:
        n = len(q)
        for i in range(n):
            # popping mechanism
            if (l % 2 == 0):
                temp = q[-1]
                q.pop()
            else:
                temp = q[0]
                q.popleft()
 
            # pushing mechanism
            if (l % 2 != 0):
                if (temp.right):
                    q.append(temp.right)
                    v.append(temp.right.data)
                if (temp.left):
                    q.append(temp.left)
                    v.append(temp.left.data)
            elif (l % 2 == 0):
                if (temp.left):
                    q.appendleft(temp.left)
                    v.append(temp.left.data)
                if (temp.right):
                    q.appendleft(temp.right)
                    v.append(temp.right.data)
        l+=1 # level plus one
    return v

# vector to store the traversal order.
v = []

# create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("ZigZag Order traversal of binary tree is")

v = zigZagTraversal(root)

for i in range(len(v)):
    print(v[i], end = " ")
    
