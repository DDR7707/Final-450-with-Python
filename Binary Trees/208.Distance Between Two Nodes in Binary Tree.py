class Solution:
    def findDist(self,root,a,b):
    
        #return: minimum distance between a and b in a tree with given root
        #code here
        
        def lca(node,a,b):
            if not node:
                return None
            
            if node.data == a or node.data == b:
                return node
            
            left = lca(node.left , a , b)
            right = lca(node.right , a , b)
            
            if left != None and right != None:
                return node
            else:
                return left or right
        
        def distance(node , d , i , level):
            if not node:
                return
            
            if node.data == i:
                d.append(level)
                return 
            
            distance(node.left , d, i , level+1)
            distance(node.right , d , i , level+1)
        
        lca = lca(root,a,b)
        d1 = []
        d2 = []
        distance(lca , d1 , a , 0)
        distance(lca , d2 , b , 0)
        return d1[0] + d2[0]
