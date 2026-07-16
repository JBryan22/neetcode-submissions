class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        if len(edges) != n - 1:
            return False
        
        visited = set()
        stack = [edges[0][0]]

        while stack:
            node = stack.pop()
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    stack.append(nei)
        
        return len(visited) == n