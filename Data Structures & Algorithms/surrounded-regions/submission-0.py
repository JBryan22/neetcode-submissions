class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROW_LENGTH = len(board)
        COL_LENGTH = len(board[0])
        def isEdge(r,c,grid):
            return r == 0 or c == 0 or r == ROW_LENGTH -1 or c == COL_LENGTH -1

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    def traverse(r,c,grid,isSurroundable):
                        if r < 0 or c < 0 or r >= ROW_LENGTH or c >= COL_LENGTH or (r,c) in visited or board[r][c] != "O":
                            return isSurroundable
                        if isEdge(r,c,grid):
                            isSurroundable = False
                        
                        visited.add((r,c))

                        isSurroundable = (isSurroundable
                        and traverse(r-1, c, grid, isSurroundable)
                        and traverse(r+1, c, grid, isSurroundable)
                        and traverse(r, c+1, grid, isSurroundable)
                        and traverse(r, c-1, grid, isSurroundable))

                        if isSurroundable:
                            grid[r][c] = 'X'

                        return isSurroundable
                    traverse(r,c,board,True)
                    
                    

