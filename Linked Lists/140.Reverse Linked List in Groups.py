"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        prev = None
        cur = head
        next = None
        c = 0
        
        while cur and c < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            c += 1
        
        if next:
            head.next = self.reverse(next , k)
        
        return prev  
