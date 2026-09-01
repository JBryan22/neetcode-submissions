# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ll in lists:
            if ll:
                heapq.heappush(heap, NodeWrapper(ll))
        
        dummyHead = ListNode(0, None)
        curr = dummyHead
        while heap:
            nodeWrapper = heapq.heappop(heap)
            curr.next = nodeWrapper.node
            curr = curr.next
            if nodeWrapper.node.next:
                heapq.heappush(heap, NodeWrapper(nodeWrapper.node.next))
        return dummyHead.next