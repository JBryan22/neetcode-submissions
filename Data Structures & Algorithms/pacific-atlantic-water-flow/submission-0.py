class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def traverse(r,c, visited, prevHeight):
            if (r,c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]) or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            
            traverse(r-1,c,visited,heights[r][c])
            traverse(r+1,c,visited,heights[r][c])
            traverse(r,c+1,visited,heights[r][c])
            traverse(r,c-1,visited,heights[r][c])

        for r in range(len(heights)):
            traverse(r,0,pacific,heights[r][0])
            traverse(r,cols-1,atlantic,heights[r][cols-1])
        for c in range(len(heights[0])):
            traverse(0, c, pacific, heights[0][c])
            traverse(rows -1, c, atlantic, heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res