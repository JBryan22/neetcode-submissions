class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i, row in enumerate(board[0]):
            for j, col in enumerate(board[1]):
                boardNum = board[i][j]
                if boardNum == '.':
                    continue
                if boardNum in rows[i] or boardNum in cols[j] or boardNum in squares[i // 3, j // 3]:
                    return False
                rows[i].add(boardNum)
                cols[j].add(boardNum)
                squares[i // 3, j // 3].add(boardNum)
        return True
