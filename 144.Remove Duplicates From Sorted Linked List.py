def removeDuplicates(head):
    #code here
    if not head or not head.next:
        return
    cur = head
    
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        
        else:
            cur = cur.next
    
    return 
