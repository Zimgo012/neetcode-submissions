# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #recursive solution
        
        #base case
        if not head:
            return None
        
        newHead = head #temp: set first element as new head
        if head.next:
            newHead = self.reverseList(head.next) #until last element
            head.next.next = head # 1 <-> 2
        head.next = None # 1 <- 2

        return newHead