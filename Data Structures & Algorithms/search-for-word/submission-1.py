class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def pathExists(x: int, y: int, curr_str: List[str]):
            if len(curr_str) >= len(word):
                return True
            
            looking_for = word[len(curr_str)]

            for dr, dc in directions:
                if x + dr < 0 or y + dc < 0 or x + dr >= ROWS or y + dc >= COLS or board[x+dr][y+dc] != looking_for:
                    continue
                curr_str.append(looking_for)
                visited.add(looking_for)
                if pathExists(x+dr, y+dc, curr_str):
                    return True
                else:
                    curr_str.pop()
                    visited.remove(looking_for)
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited.add(word[0])
                    if pathExists(r, c, [word[0]]):
                        return True
                    visited.remove(word[0])
        return False