#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Iterative
        pre = None
        cur = head
        nex = None
        
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
            
        return pre  
        
        # Recursive
        if head is None or head.next is None:
            return head
        
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rest
