# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        tb = 0
        for ll in lists:
            if ll:
                heapq.heappush(heap, (ll.val, tb, ll))
                tb+=1
        
        dummyHead = ListNode(0, None)
        curr = dummyHead
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, tb, node.next))
                tb+=1
        return dummyHead.next