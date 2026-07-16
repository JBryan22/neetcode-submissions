class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited=set()
        stack = [(0, -1)]

        while stack:
            curr, parent = stack.pop()

            visited.add(curr)

            for nei in adj_list[curr]:
                if nei not in visited:
                    stack.append((nei,curr))
                elif nei != parent:
                    return False
        
        if len(visited) != n:
            return False
        
        return True
