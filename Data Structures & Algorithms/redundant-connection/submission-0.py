class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        for a,b in edges:
            if a in visited and b in visited:
                return [a,b]
            visited.add(a)
            visited.add(b)
        return []