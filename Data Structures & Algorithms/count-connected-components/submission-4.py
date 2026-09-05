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

            while stack:
                innerNode = stack.pop()
                visited.add(innerNode)
                for nei in adjList[innerNode]:
                    if nei not in visited:
                        stack.append(nei)
            count += 1
        return count
            
