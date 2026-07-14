class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(0,(0,0))]
        ROW_LENGTH = len(grid)
        COL_LENGTH = len(grid[0])

        time = 0
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

        while minHeap:
            _, rc = heapq.heappop(minHeap)
            (r, c) = rc
            if grid[r][c] > time:
                time = grid[r][c]
            
            grid[r][c] = -1 
            if r == ROW_LENGTH - 1 and c == COL_LENGTH - 1:
                return time
            for dr, dc in directions:
                if not (r + dr < 0 or r + dr >= ROW_LENGTH or c + dc < 0 or c + dc >= COL_LENGTH or grid[r + dr][c + dc] == -1):
                    heapq.heappush(minHeap, (grid[r+dr][c+dc],(r + dr, c + dc)))
        
        return time

