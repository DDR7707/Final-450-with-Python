#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        if not head or not head.next:
            return head
            
        cur = head
        while cur.next:
            if cur.data < cur.next.data:
                cur.data = cur.next.data
                cur.next = cur.next.next
            
            else:
                cur = cur.next
        
        return head 
