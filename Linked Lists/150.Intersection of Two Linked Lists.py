def intersetPoint(head1,head2):
    #code here
    cur1 = head1
    cur2 = head2
    if cur1 == None or cur2 == None:
        return -1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
        
        # if cur1 == cur2:
        #     return cur1.data
        
        if cur1 == None:
            cur1 = head2
        if cur2 == None:
            cur2 = head1
    
    return cur2.data 
