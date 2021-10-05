class newNode:
 
    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# function to generate array of ancestors
def generateArray(root, ancestors):
 
    # There will be no ancestor of root node
    ancestors[root.data] = -1
 
    # level order traversal to
    # generate 1st ancestor
    q = []
    q.append(root)
 
    while(len(q)):
        temp = q[0]
        q.pop(0)
 
        if (temp.left):
            ancestors[temp.left.data] = temp.data
            q.append(temp.left)
     
        if (temp.right):
            ancestors[temp.right.data] = temp.data
            q.append(temp.right)
 
# function to calculate Kth ancestor
def kthAncestor(root, n, k, node):
     
    # create array to store 1st ancestors
    ancestors = [0] * (n + 1)
 
    # generate first ancestor array
    generateArray(root,ancestors)
 
    # variable to track record of number
    # of ancestors visited
    count = 0
 
    while (node != -1) :
        node = ancestors[node]
        count += 1
        if(count == k):
            break
             
    # prKth ancestor
    return node
                         
# Driver Code
if __name__ == '__main__':
 
    # Let us create binary tree shown
    # in above diagram
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
     
    k = 2
    node = 5
 
    # prkth ancestor of given node
    print(kthAncestor(root, 5, k, node))
    
    
    
    
    
    
    class node:
     
    def __init__(self, data):
         
        self.left = None
        self.right = None
        self.data = data
 
# Program to find kth ancestor
def ancestor(root, item):
     
    global k
     
    if (root == None):
        return False
     
    # Element whose ancestor is
    # to be searched
    if (root.data == item):
         
        # Reduce count by 1
        k = k - 1
        return True
   
    else:
  
        # Checking in left side
        flag = ancestor(root.left, item);
         
        if (flag):
            if (k == 0):
                 
                # If count = 0 i.e. element is found
                print("[" + str(root.data) + "]", end = ' ')
                return False
         
            # If count !=0 i.e. this is not the
            # ancestor we are searching for
            # so decrement count
            k = k - 1
            return True
     
        # Similarly Checking in right side
        flag2 = ancestor(root.right, item)
         
        if (flag2):
            if (k == 0):
                print("[" + str(root.data) + "]")
                return False
       
            k = k - 1
            return True
 
# Driver code
if __name__=="__main__":
     
    root = node(1)
    root.left = node(4)
    root.left.right = node(7)
    root.left.left = node(3)
    root.left.right.left = node(8)
    root.right = node(2)
    root.right.right = node(6)
     
    item = 3
    k = 1
    loc = k
    flag = ancestor(root, item)
     
    if (flag):
        print("Ancestor doesn't exist")
    else:
        print("is the " + str(loc) +
              "th ancestor of [" + str(item) + "]")
        
        
        
        
        
        
 
class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# recursive function to calculate
# Kth ancestor
def kthAncestorDFS(root, node, k):
     
    # Base case
    if (not root):
        return None
     
    if (root.data == node or
       (kthAncestorDFS(root.left, node, k)) or
       (kthAncestorDFS(root.right, node, k))):
         
        if (k[0] > 0):
            k[0] -= 1
         
        elif (k[0] == 0):
             
            # print the kth ancestor
            print("Kth ancestor is:", root.data)
             
            # return None to stop further
            # backtracking
            return None
             
        # return current node to previous call
        return root
     
# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
 
    k = [2]
    node = 5
 
    # prkth ancestor of given node
    parent = kthAncestorDFS(root,node,k)
     
    # check if parent is not None, it means
    # there is no Kth ancestor of the node
    if (parent):
        print("-1")
