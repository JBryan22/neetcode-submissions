class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word:str):
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
    
    def search(self, word: str):
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            else:
                return False
        return node.isWord

    def prefixSearch(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c in node.children:
                node = node.children[c]
                continue
            else:
                return False
        return True

    def prefixSearchNode(self, prefix: str) -> Optional[TrieNode]:
        node = self.root

        for c in prefix:
            if c in node.children:
                node = node.children[c]
                continue
            else:
                return None
        return node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        res = []
        visited = set()
        resSet = set()
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(row: int, col: int, currStr: List[str], node: TrieNode):
            if node.isWord:
                word = "".join(currStr)
                if word not in resSet:
                    resSet.add("".join(currStr))
                    res.append(word)

            for dr, dc in directions:
                if (
                    dr + row < 0 or 
                    dc + col < 0 or 
                    dr + row >= ROWS or 
                    dc + col >= COLS or 
                    (dr+row, dc+col) in visited or 
                    board[row+dr][col+dc] not in node.children
                ):
                    continue
                newRow, newCol, newChar = row+dr, col+dc, board[row+dr][col+dc]
                visited.add((newRow, newCol))
                currStr.append(newChar)
                dfs(newRow, newCol, currStr, node.children[newChar])
                currStr.pop()
                visited.remove((newRow, newCol))

        for r in range(ROWS):
            for c in range(COLS):
                node = trie.prefixSearchNode(board[r][c])
                if node != None:
                    visited.add((r,c))
                    dfs(r,c,[board[r][c]],node)
                    visited = set()
        return res
        

                