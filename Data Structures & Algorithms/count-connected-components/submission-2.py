class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj_list = defaultdict(list)

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        for n in adj_list.keys():
            if n in visited:
                continue
            stack = [n]
            visited.add(n)

            while stack:
                node = stack.pop()

                for nei in adj_list[node]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            
            res += 1

        for i in range(n):
            if i not in visited:
                res += 1
        
        return res