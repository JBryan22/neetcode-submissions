class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_length = len(image)
        col_length = len(image[0])
        og_color = image[sr][sc]
        if color == og_color:
            return image

        def fill(sr: int, sc: int):
            if sr < 0 or sc < 0:
                return
            if sr >= row_length or sc >= col_length:
                return

            if image[sr][sc] != og_color:
                return
            
            image[sr][sc] = color

            fill(sr - 1, sc)
            fill(sr + 1, sc)
            fill(sr, sc + 1)
            fill(sr, sc - 1)

        fill(sr, sc)
        return image