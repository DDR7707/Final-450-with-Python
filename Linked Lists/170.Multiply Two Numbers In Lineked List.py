class Node:
       
    # Function to initialize the node 
    def __init__(self, data):
         
        self.data = data
        self.next = None
       
# Linked List Class
class LinkedList:
   
    # Function to initialize the
    # LinkedList class.
    def __init__(self):
   
        # Initialize head as None
        self.head = None
   
    # Function to insert a node at the
    # beginning of the Linked List
    def push(self, new_data):
       
        # Create a new Node
        new_node = Node(new_data)
   
        # Make next of the new Node as head
        new_node.next = self.head
   
        # Move the head to point to new Node
        self.head = new_node
           
    # Function to print the Linked List
    def printList(self):
         
        ptr = self.head
   
        while (ptr != None):
            print(ptr.data, end = '')
            if ptr.next != None:
                print('->', end = '')
                 
            ptr = ptr.next
               
        print()
   
# Multiply contents of two Linked Lists
def multiplyTwoLists(first, second):
   
    num1 = 0
    num2 = 0
 
    first_ptr = first.head
    second_ptr = second.head
     
    while first_ptr != None or second_ptr != None:
        if first_ptr != None:
            num1 = (num1 * 10) + first_ptr.data
            first_ptr = first_ptr.next
     
        if second_ptr != None:
            num2 = (num2 * 10) + second_ptr.data
            second_ptr = second_ptr.next
     
    return num1 * num2
   
# Driver code
if __name__=='__main__':
   
    first = LinkedList()
    second = LinkedList()
   
    # Create first Linked List 9->4->6
    first.push(6)
    first.push(4)
    first.push(9)
 
    # Printing first Linked List
    print("First list is: ", end = '')
    first.printList()
   
    # Create second Linked List 8->4
    second.push(4)
    second.push(8)
 
    # Printing second Linked List
    print("Second List is: ", end = '')
    second.printList()
   
    # Multiply two linked list and
    # print the result
    result = multiplyTwoLists(first, second)
    print("Result is: ", result)
    
    
    
    
    
    
    '''
    For every number in ll2 , multiply it with every number og ll1 , if carry generated ,  add it to next number and at last create new node with carry
    
    For every number in ll2 , add dummy variable of 0 in front of that number process.
    
    Finally add all the linked lists
    
    '''
