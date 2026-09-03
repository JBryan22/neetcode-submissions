class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()

        def containsWord(row: int, col: int, curr_str: List[str]):
            if len(curr_str) == len(word):
                return True
            
            looking_for = word[len(curr_str)]

            for dr, dc in directions:
                if ((row+dr,col+dc) in visited or 
                    row + dr < 0 or 
                    row + dr >= ROWS or 
                    col + dc < 0 or 
                    col + dc >= COLS or 
                    board[row+dr][col+dc] != looking_for):
                    continue

                curr_str.append(looking_for)
                visited.add((row+dr, col+dc))
                if containsWord(row+dr, col+dc, curr_str):
                    return True
                else:
                    curr_str.pop()
                    visited.remove((row+dr, col+dc))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited.add((row,col))
                    if containsWord(row,col,[word[0]]):
                        return True
                    visited.remove((row,col))
        
        return False
