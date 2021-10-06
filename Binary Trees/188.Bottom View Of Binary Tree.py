class Node:
     
    def __init__(self, key = None,
                      left = None,
                     right = None):
                          
        self.data = key
        self.left = left
        self.right = right
         
def printBottomView(root):
     
      # Create a dictionary where
    # key -> relative horizontal distance
    # of the node from root node and
    # value -> pair containing node's
    # value and its level
    d = dict()
     
    printBottomViewUtil(root, d, 0, 0)
     
    # Traverse the dictionary in sorted
    # order of their keys and print
    # the bottom view
    for i in sorted(d.keys()):
        print(d[i][0], end = " ")
 
def printBottomViewUtil(root, d, hd, level):
     
      # Base case
    if root is None:
        return
     
    # If current level is more than or equal
    # to maximum level seen so far for the
    # same horizontal distance or horizontal
    # distance is seen for the first time,
    # update the dictionary
    if hd in d:
        if level >= d[hd][1]:
            d[hd] = [root.data, level]
    else:
        d[hd] = [root.data, level]
         
    # recur for left subtree by decreasing
    # horizontal distance and increasing
    # level by 1
    printBottomViewUtil(root.left, d, hd - 1,
                                   level + 1)
     
    # recur for right subtree by increasing
    # horizontal distance and increasing
    # level by 1
    printBottomViewUtil(root.right, d, hd + 1,
                                    level + 1)
 
# Driver Code   
if __name__ == '__main__':
     
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
     
    print("Bottom view of the given binary tree :")
     
    printBottomView(root)
















class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.hd = 1000000
        self.left = None
        self.right = None
  
# Method that prints the bottom view.
def bottomView(root):
 
    if (root == None):
        return
     
    # Initialize a variable 'hd' with 0
    # for the root element.
    hd = 0
     
    # TreeMap which stores key value pair
    # sorted on key value
    m = dict()
  
    # Queue to store tree nodes in level
    # order traversal
    q = []
  
    # Assign initialized horizontal distance
    # value to root node and add it to the queue.
    root.hd = hd
     
    # In STL, append() is used enqueue an item
    q.append(root) 
  
    # Loop until the queue is empty (standard
    # level order loop)
    while (len(q) != 0):
        temp = q[0]
         
        # In STL, pop() is used dequeue an item
        q.pop(0) 
         
        # Extract the horizontal distance value
        # from the dequeued tree node.
        hd = temp.hd
  
        # Put the dequeued tree node to TreeMap
        # having key as horizontal distance. Every
        # time we find a node having same horizontal
        # distance we need to replace the data in
        # the map.
        m[hd] = temp.data
  
        # If the dequeued node has a left child, add
        # it to the queue with a horizontal distance hd-1.
        if (temp.left != None):
            temp.left.hd = hd - 1
            q.append(temp.left)
  
        # If the dequeued node has a right child, add
        # it to the queue with a horizontal distance
        # hd+1.
        if (temp.right != None):
            temp.right.hd = hd + 1
            q.append(temp.right)
  
    # Traverse the map elements using the iterator.
    for i in sorted(m.keys()):
        print(m[i], end = ' ')
         
# Driver Code
if __name__=='__main__':
     
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
     
    print("Bottom view of the given binary tree :")
     
    bottomView(root)
