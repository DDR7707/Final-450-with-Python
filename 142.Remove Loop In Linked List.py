def remove(head):
  slow = head
  fast = head
  
  while slow and fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow.data == fast.data:
      slow = head
      
      while slow.data != fast.data:
        slow = slow.next
        fast = fast.next
      
      fast.next = None
   return head   
