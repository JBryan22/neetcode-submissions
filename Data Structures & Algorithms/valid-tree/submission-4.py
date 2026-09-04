class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        if len(edges) != n - 1:
            return False

        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        stack = [edges[0][0]]
        visited = set()

        while stack:
            node = stack.pop()

            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        return len(visited) == n