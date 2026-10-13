# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        dumbNode = ListNode()
        dumbNode.next = head
        k = dumbNode

        while head:
            if head.val != 9:
                k = head
            head = head.next
        
        k.val += 1
        k = k.next

        while k:
            k.val = 0
            k = k.next

        return dumbNode if dumbNode.val else dumbNode.next
