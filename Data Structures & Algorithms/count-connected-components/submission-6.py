class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adjList = defaultdict(list)

        for node1, node2 in edges: 
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        visited = set()

        for node in adjList:
            if node in visited:
                continue
            
            stack = [node]
            visited.add(node)

            while stack:
                innerNode = stack.pop()
                for nei in adjList[innerNode]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            count += 1
        for i in range(n):
            if i not in visited:
                count += 1
        return count
            
