#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        look = set()
        if not head or not head.next:
            return head
        
        look.add(head.data)
        prev = head
        cur = head.next
        
        while cur:
            if cur.data in look:
                cur = cur.next
            else:
                look.add(cur.data)
                prev.next = cur
                perv = cur
                cur = cur.next
        prev.next = None        
        return head
      
      
      

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        look = set()
        if not head or not head.next:
            return head
        
        cur = head
        look.add(cur.data)
        
        while cur.next:
            if cur.next.data in look:
                cur.next = cur.next.next
            else:
                look.add(cur.next.data)
                cur = cur.next
        
        return head        
    
