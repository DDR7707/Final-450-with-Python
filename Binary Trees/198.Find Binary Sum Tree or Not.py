'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
class Solution:
    def isSumTree(self,root):
        # Code here
        if not root:
            return True
        if root.left == None and root.right == None:
            return True
            
        sum = 0
        if root.left:
            sum += root.left.data
        
        if root.right:
            sum += root.right.data
        
        return root.data == sum and self.isSumTree(root.left) and self.isSumTree(root.right)
      
      
      
      
      
      
      
      # Second Version
      
      class node:
 
    def __init__(self, x):
 
        self.data = x
        self.left = None
        self.right = None
 
 
def isLeaf(node):
 
    if(node == None):
        return 0
    if(node.left == None and node.right == None):
        return 1
    return 0
 
# A utility function to get the sum
# of values in tree with root as root
def sum(root):
 
    if(root == None):
        return 0
    return (sum(root.left) +
            root.data +
            sum(root.right))
 
 
# returns 1 if SumTree property holds
# for the given tree
def isSumTree(node):
   
    # If node is None or
    # it's a leaf node then return true
    if(node == None or isLeaf(node)):
        return 1
 
    if(isSumTree(node.left) and isSumTree(node.right)):
       
        # Get the sum of nodes in left subtree
        if(node.left == None):
            ls = 0
        elif(isLeaf(node.left)):
            ls = node.left.data
        else:
            ls = 2 * (node.left.data)
 
        # Get the sum of nodes in right subtree
        if(node.right == None):
            rs = 0
        elif(isLeaf(node.right)):
            rs = node.right.data
        else:
            rs = 2 * (node.right.data)
 
        # If root's data is equal to sum of nodes
        # in left and right subtrees then return 1
        # else return 0
        return(node.data == ls + rs)
 
    return 0
 
# Driver code
if __name__ == '__main__':
 
    root = node(26)
    root.left = node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)
 
    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")
