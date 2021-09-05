''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

def findIntersection(head1,head2):
    #return head
    final = []
    cur1 = head1
    cur2 = head2
    
    while cur1 and cur2:
        if cur1.data == cur2.data:
            final.append(Node(cur1.data))
            cur1 = cur1.next
            cur2 = cur2.next
        
        elif cur1.data < cur2.data:
            cur1 = cur1.next
        
        else:
            cur2 = cur2.next
            
    head = final[0]
    for i in range(len(final)-1):
        final[i].next = final[i+1]
    
    return head
        
