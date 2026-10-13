# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        #reverselist
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        # remove n
        dumbNode = ListNode()
        dumbNode.next = prev
        tail = dumbNode
        i = 1
        
        while i != n:
            tail = prev
            prev = prev.next
            i += 1
        
        tail.next = prev.next

        #Reverse again
        curr = dumbNode.next
        prev2 = None
        while curr:
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
        
        return prev2






       

             
