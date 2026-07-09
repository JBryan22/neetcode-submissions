class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        def islandSpan(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited or grid[r][c] != "1":
                return
            visited.add((r,c))
            islandSpan(r + 1, c)
            islandSpan(r - 1, c)
            islandSpan(r, c + 1)
            islandSpan(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islandSpan(r, c)
                    count += 1
        
        return count


