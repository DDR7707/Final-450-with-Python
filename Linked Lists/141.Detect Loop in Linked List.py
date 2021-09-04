class Node:
  def __init__(self,head,next):
    self.head = head
    self.next = None
  
  def detect_loop(self):
    slow = self.head
    fast = self.head
    
    while slow and fast and fast.next:
      if slow == fast:
        return True
      slow = slow.next
      fast = fast.next.next
      
    return False
