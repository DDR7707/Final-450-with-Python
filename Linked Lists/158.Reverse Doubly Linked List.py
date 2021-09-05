'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    #return head after reversing
    cur = head
    pre = None
    
    while cur:
        pre = cur.prev
        cur.prev = cur.next
        cur.next = pre
        if cur.prev:
            cur = cur.prev
        else:
            return cur
