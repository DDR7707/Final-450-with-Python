class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        def count(root):
            if not root:
                return 0
            
            return count(root.left) + count(root.right) + 1
        
        arr = []*count(root)
        
        def inorder(root,arr):    
            if root:
                inorder(root.left,arr)
                arr.append(root.data)
                inorder(root.right,arr)
        
        inorder(root,arr) 
        
        arr.sort()
        
        def final(root,arr):
            if root:
                final(root.left,arr)
                root.data = arr.pop(0)
                final(root.right,arr)
        
        final(root,arr)
        return root
