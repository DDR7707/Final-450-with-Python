class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        x = preorder.pop(0)
        ind = inorder.index(x)
        root = TreeNode(x)
        
        root.left = self.buildTree(preorder , inorder[:ind])
        root.right = self.buildTree(preorder , inorder[ind+1:])
        
        return root
