class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()

        if image[sr][sc] == color:
            return image

        def dfs(r, c, col):
            if (r,c) in visited or r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != col:
                return
            
            image[r][c] = color
            visited.add((r,c))

            dfs(r+1,c, col)
            dfs(r-1,c, col)
            dfs(r,c+1, col)
            dfs(r,c-1, col)
        
        dfs(sr,sc,image[sr][sc])

        return image
