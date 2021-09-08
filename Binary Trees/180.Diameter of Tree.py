class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def height(self , root , ans):
        if not root:
            return 0
        
        left = self.height(root.left , ans)
        right = self.height(root.right , ans)
        
        ans[0] = max(ans[0] , 1+left+right)
        return 1+max(left , right)
        
    def diameter(self,root):
        # Code here
        ans = [-1]
        self.height(root , ans)
        return ans[0]
