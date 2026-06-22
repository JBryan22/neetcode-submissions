"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        mapOfNodes = {}
        ogHead = head
        while(head):
            mapOfNodes[head] = Node(head.val)
            head = head.next
        newHead = mapOfNodes.get(ogHead)
        while(ogHead):
            node = mapOfNodes.get(ogHead)
            node.next = mapOfNodes.get(ogHead.next)
            node.random = mapOfNodes.get(ogHead.random)
            ogHead = ogHead.next
        return newHead