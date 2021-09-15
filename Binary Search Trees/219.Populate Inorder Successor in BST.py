def populateNext(node):
 
    # The first visited node will be the rightmost node
    # next of the rightmost node will be NULL
    populateNextRecur(node, next)
 
# /* Set next of all descendants of p by
# traversing them in reverse Inorder */
def populateNextRecur(p, next_ref):
     
    if (p != None):
         
        # First set the next pointer in right subtree
        populateNextRecur(p.right, next_ref)
 
        # Set the next as previously visited node in reverse Inorder
        p.next = next_ref
 
        # Change the prev for subsequent node
        next_ref = p
 
        # Finally, set the next pointer in right subtree
        populateNextRecur(p.left, next_ref)
