class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    stack = [(row,col)]

                    while stack:
                        r,c = stack.pop()

                        grid[r][c] = 'X'

                        for dr, dc in directions:
                            if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or grid[r+dr][c+dc] != '1':
                                continue
                            stack.append((r+dr,c+dc))
                    
                    res += 1
        return res