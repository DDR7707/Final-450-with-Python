class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        def solve(node):
            if not node:
                return (1,0)
        
            left = solve(node.left)
            right = solve(node.right)
        
            if left[0] == right[0]:
                return (left[0]+1 , max(right[1] , left[1])+node.data)
            elif left[0] > right[0]:
                return (left[0]+1 , left[1]+node.data)
            else:
                return (right[0]+1 , right[1]+node.data)
        
        return solve(root)[1] 
