class newNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def solve(root):
    final = []
    def foo(node , final):
        if not node:
            return 0
        
        left = foo(node.left , final)
        right = foo(node.right , final)
        added = left+right+node.key
        
        final.append(added)
        
        return added
    
    foo(root , final)
    return max(final)

if __name__ == '__main__':
     
    '''
               1
               
          -2       3
          
        4    5  -6   2
    '''
    root = newNode(1)
    root.left = newNode(-2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(-6)
    root.right.right = newNode(2)
 
    print(solve(root))
