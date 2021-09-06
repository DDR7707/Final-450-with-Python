class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        if not root:
            return root
        
        final = [root.data]
        que = [root]
        
        while que:
            temp = que.pop(0)
            if temp.left:
                final.append(temp.left.data)
                que.append(temp.left)
            
            if temp.right:
                final.append(temp.right.data)
                que.append(temp.right)
        
        return final  
