class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.next = None
        self.prev = None
 
def ll3sum(head , x):
    final = 0
    cur = head
    last = head
    
    while last.next:
        last = last.next
        
    while cur.next:
        l = cur.next
        r = last
        
 
        while l.data < r.data:
            print(cur.data , l.data , r.data)
            add = cur.data + l.data + r.data
            print(add)
            
            if add == x:
                final += 1
                l = l.next
            
            elif add < x:
                l = l.next
            
            else:
                r = r.prev
        print("\n\n")
        cur = cur.next        
        
    return final    
    
def insert(head, data):

    temp = Node(data)
    if (head == None):
        head = temp
    else:
        temp.next = head
        head.prev = temp
        head = temp
         
    return head

if __name__ == '__main__':
    head = None
    head = insert(head, 9)
    head = insert(head, 8)
    head = insert(head, 6)
    head = insert(head, 5)
    head = insert(head, 4)
    head = insert(head, 2)
    head = insert(head, 1)
    
    x = 17
    
    print(ll3sum(head , x))
