#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    if not head:
        return None
    
    cur = head
    for i in range(n):
        if cur:
            cur = cur.next
        else:
            return -1
    
    while cur:
        head = head.next
        cur = cur.next
    
    return head.data 
