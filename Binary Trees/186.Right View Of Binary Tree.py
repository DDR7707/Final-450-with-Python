class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        
        # code here
        if not root:
            return []
        final = [root.data]
        que = [root]
        
        while que:
            new = []
            for i in que:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            
            if new:
                final.append(new[-1].data)
            que = new
            
        return final    
        
