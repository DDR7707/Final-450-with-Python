#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    if not head:
        return True
    
    cur = head
    while cur:
        if cur.next == head:
            return True
        cur = cur.next    
    return False        
