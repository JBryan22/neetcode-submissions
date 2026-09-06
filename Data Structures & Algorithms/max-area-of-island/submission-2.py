class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack = [(r,c)]
                    visited.add((row,col))
                    area = 0
                    while stack:
                        row, col = stack.pop()
                        area += 1

                        for dr, dc in directions:
                            newRow, newCol = row + dr, col + dc
                            if (newRow, newCol) in visited or newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or grid[newRow][newCol] != 1:
                                continue
                            stack.append((newRow, newCol))
                            visited.add((newRow,newCol))
                    res = max(res, area)
        
        return res