'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        #code here
        slow = head
        fast = head
        
        while fast.next != head.data and fast.next.next != head.data:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next.next == head:
            fast = fast.next
        
        head1 = head
        head2 = slow.next        
        fast.next = slow.next
        slow.next = head
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2
