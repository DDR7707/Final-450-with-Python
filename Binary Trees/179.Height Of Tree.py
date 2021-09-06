# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if not root:
            return 0
        
        return max(self.height(root.left)+1 , self.height(root.right)+1) 
