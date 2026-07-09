class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0
        visited = set()

        def islandSpan(r, c) -> int:
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            count = 1
            visited.add((r,c))
            count += islandSpan(r + 1, c)
            count += islandSpan(r - 1, c)
            count += islandSpan(r, c + 1)
            count += islandSpan(r, c - 1)

            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxIsland = max(maxIsland, islandSpan(r,c))

        return maxIsland