class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROW_LENGTH = len(board)
        COL_LENGTH = len(board[0])

        def traverse(r,c):

            if r < 0 or c < 0 or r >= ROW_LENGTH or c >= COL_LENGTH or (r,c) in visited or board[r][c] != "O":
                return

            board[r][c] = "S"
            visited.add((r,c))

            traverse(r-1, c)
            traverse(r+1, c)
            traverse(r, c+1)
            traverse(r, c-1)



        for r in range(len(board)):
            if board[r][0] == "O" and (r,0) not in visited:
                traverse(r, 0)
            if board[r][COL_LENGTH - 1] == "O" and (r, COL_LENGTH - 1) not in visited:
                traverse(r, COL_LENGTH - 1)

        for c in range(len(board[0])):
            if board[0][c] == "O" and (0,c) not in visited:
                traverse(0, c)
            if board[ROW_LENGTH - 1][c] == "O" and (ROW_LENGTH -1, c) not in visited:
                traverse(ROW_LENGTH - 1, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"