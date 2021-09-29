class Solution:
    def divide(self, N, head):
        # code here
        evenstart = None
        evenend = None
        oddstart = None
        oddend = None
        cur = head
        
        while cur:
            if cur.data %2 == 0:
                if evenstart == None:
                    evenstart = cur
                    evenend = evenstart
                else:
                    evenend.next = cur
                    evenend = evenend.next
            else:
                if oddstart == None:
                    oddstart = cur
                    oddend = oddstart
                else:
                    oddend.next = cur
                    oddend = oddend.next
            cur = cur.next
        
        if oddstart == None or evenstart == None:
            return head
        
        evenend.next = oddstart
        oddend.next = None
        
        head = evenstart
        return head
