class Solution:
    def isBalanced(self,root):
    
        #add code here
        self.final = True
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            if abs(left - right) > 1:
                self.final = False
            
            return max(left , right)+1
        
        check(root)
        return self.final
