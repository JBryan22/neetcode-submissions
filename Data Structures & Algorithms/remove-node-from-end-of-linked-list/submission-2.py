# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next

        placement = length - n
        if placement < 1:
            return None
        curr = head
        while placement > 1:
            curr = head.next
            placement -= 1
        curr.next = curr.next.next
        return head