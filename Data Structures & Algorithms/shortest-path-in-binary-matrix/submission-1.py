class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = 1
        queue = deque()
        visited = set()
        visited.add((0,0))
        if grid[0][0] != 0:
            return -1
        queue.append((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0 
                    or r + dr >= len(grid) or c + dc >= len(grid[0]) 
                    or (r + dr,c + dc) in visited 
                    or grid[r + dr][c + dc] != 0):
                        continue
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))
                
            length += 1
        return length