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
        cur.next = pre
        cur.prev =cur.next
        pre = cur
        if cur.prev:
            cur = cur.prev
        else:
            return cur
    
# Above is not correct

def reverse(self):
  temp = None
  current = self.head
  
  while current is not None:
    temp = current.prev
    current.prev = current.next
    current.next = temp
    current = current.prev
 
  if temp is not None:
    self.head = temp.prev
