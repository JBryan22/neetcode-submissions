class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW_COUNT = len(grid)
        COL_COUNT = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited_outer = set()
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 2147483647:
                    queue = deque()
                    visited = set()
                    def traverseIsland(grid, r, c):
                        if grid[r][c] == 0 and (r,c) not in visited_outer:
                            queue.append((0, (r,c)))
                        
                        visited.add((r,c))
                        visited_outer.add((r,c))

                        for dr, dc in directions:
                            if r + dr < 0 or c + dc < 0 or r + dr >= ROW_COUNT or c + dc >= COL_COUNT or (r + dr, c + dc) in visited or grid[r+dr][c+dc] == -1:
                                continue
                            traverseIsland(grid, r + dr, c + dc)
                    
                    traverseIsland(grid, r, c)
                    visited = set()
                    for d, point in queue:
                        visited.add(point)
                    while queue:
                        d, point = queue.popleft()
                        r, c = point
                        grid[r][c] = d
                        for dr, dc in directions:
                            if r + dr < 0 or c + dc < 0 or r + dr >= ROW_COUNT or c + dc >= COL_COUNT or (r + dr, c + dc) in visited or grid[r+dr][c+dc] == -1:
                                continue
                            queue.append((d+1, (r+dr,c+dc)))
                            visited.add((r+dr,c+dc))
        
                                
                        