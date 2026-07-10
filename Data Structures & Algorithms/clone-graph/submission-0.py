"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        og = {node: Node(node.val)}

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                if neighbor not in og:
                    og[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                og[n].neighbors.append(og[neighbor])
            
        return og[node]

