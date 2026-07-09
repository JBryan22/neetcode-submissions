class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        time = 0
        lastRot = -1

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue:
            fruits_rotted = False
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or grid[r + dr][c + dc] != 1:
                        continue
                    queue.append((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2
                    fruits_rotted = True

            time += 1
            if fruits_rotted:
                lastRot = time
        
        return lastRot

