"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        look = {}
        
        def dfs(s):
            if s in look:
                return look[s]
            
            temp = Node(s.val)
            look[s] = temp
            
            for i in s.neighbors:
                temp.neighbors.append(dfs(i))
            
            return temp
        
        return dfs(node) if node else None
