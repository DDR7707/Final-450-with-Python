class Node:
    def __init__(self, next = None,
                       prev = None, data = None):
        self.next = next 
        self.prev = prev 
        self.data = data
 
def push(head, new_data):
 
    new_node = Node(data = new_data)
 
    new_node.next = head
    new_node.prev = None
 
    if head is not None:
        head.prev = new_node
 
    head = new_node
    return head
 
def printList(head):
 
    node = head
 
    print("Given linked list")
    while(node is not None):
        print(node.data, end = " "),
        last = node
        node = node.next

def rotate(head,N):
    end = head
    while end.next:
        end = end.next
    
    cur = head
    pre = None
    
    for i in range(N):
        end.next = cur
        cur.prev = end
        pre = cur
        cur = cur.next
        pre.next = None
        end = end.next
    return cur    


if __name__ == "__main__":
    head = None
    head = push(head, 'h')
    head = push(head, 'g')
    head = push(head, 'f')
    head = push(head, 'e')
    head = push(head, 'd')
    head = push(head, 'c')
    head = push(head, 'b')
    head = push(head, 'a')
 
    printList(head)
    print("\n")
     
    N = 4
    head = rotate(head, N)
 
    printList(head) 
