class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)
        
        zero = zeroD
        one = oneD
        two = twoD
        
        cur = head
        while cur:
            if cur.data == 0:
                zero.next = cur
                zero = zero.next
            
            elif cur.data == 1:
                one.next = cur
                one = one.next
            
            else:
                two.next = cur
                two = two.next
            
            cur = cur.next
        
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None
        
        return zeroD.next
