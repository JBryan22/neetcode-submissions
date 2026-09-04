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
        ogNodes = {node: Node(node.val)}

        while queue:
            n = queue.popleft()

            for neigh in n.neighbors:
                if neigh not in ogNodes:
                    ogNodes[neigh] = Node(neigh.val)
                    queue.append(neigh)
                ogNodes[n].neighbors.append(ogNodes[neigh])
        return ogNodes[node]