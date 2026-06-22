"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        queue = deque([(root, 0)])

        while (queue):
            node, d = queue.popleft()
            if not node:
                continue

            if queue and queue[0][0] is not None and queue[0][1] == d:
                node.next = queue[0][0]
            
            queue.append((node.left, d+1))
            queue.append((node.right, d+1))
        
        return root