# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        final = []
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            
            s = l1.val + l2.val + carry
            
            if s > 9:
                carry = 1
                final.append(ListNode(s - 10))
            else:
                final.append(ListNode(s))
                carry = 0
                
            l1 = l1.next
            l2 = l2.next
            
        if carry != 0:
            final.append(ListNode(carry))
            
        for i in range(len(final) - 1):
            final[i].next = final[i + 1]
                           
        return final[0]
