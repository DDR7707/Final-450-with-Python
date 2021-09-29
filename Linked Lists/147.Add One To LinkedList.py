class Node():
    def __init__(self):
        self.data = None
        self.next = None
 
# Function to create a new node
def create_Node(data):
    temp = Node()
    temp.data = data
    temp.next = None
    return temp
 
# Function to print the linked list
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end = ' ')
        temp = temp.next
    print()
 
# Function to add one to a number
# represented as linked list
def addOne(head):
 
    # To store the last node in the
    # linked list which is not equal to 9
    last = None
    cur = head
 
    # Iterate till the last node
    while(cur.next != None):
        if(cur.data != 9):
            last = cur
        cur = cur.next
 
    # If last node is not equal to 9
    # add 1 to it and return the head
    if(cur.data != 9):
        cur.data += 1
        return head
 
    # If list is of the type 9 -> 9 -> 9 ...
    if(last == None):
        last = Node()
        last.data = 0
        last.next = head
        head = last
 
    # For cases when the rightmost node which
    # is not equal to 9 is not the last
    # node in the linked list
    last.data += 1
    last = last.next
 
    while(last != None):
        last.data = 0
        last = last.next
 
    return head
 
# Driver code
if __name__=='__main__':
    head = create_Node(1)
    head.next = create_Node(2)
    head.next.next = create_Node(9)
    head.next.next.next = create_Node(9)
 
    print("Original list is : ", end = "")
    printList(head)
 
    head = addOne(head)
 
    print("Resultant list is : ", end = "")
    printList(head)
