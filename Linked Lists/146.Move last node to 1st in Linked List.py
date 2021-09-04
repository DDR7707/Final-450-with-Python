def moving(head):
  if head is None or head.next is None:
    return head
  
  cur = head
  while cur.next.next:
    cur = cur.next
  start = cur.next 
  cur.next.next = head
  cur.next = None
  return start
