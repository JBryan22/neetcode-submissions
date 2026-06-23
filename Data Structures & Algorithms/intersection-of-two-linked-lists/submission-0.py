# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        leftLen = 0
        rightLen = 0
        curr = headA
        while curr:
            curr = curr.next
            leftLen += 1

        curr = headB
        while curr:
            curr = curr.next
            rightLen += 1
        
        while leftLen > rightLen:
            headA = headA.next
            leftLen -= 1

        while rightLen > leftLen:
            headB = headB.next
            rightLen -= 1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None